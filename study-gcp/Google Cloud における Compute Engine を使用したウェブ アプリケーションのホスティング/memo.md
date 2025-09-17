student-02-0083996ffc99@qwiklabs.net
t0qBV9kwCpgw
qwiklabs-gcp-00-63f784539d79



gcloud config set compute/zone europe-west1-c
gcloud config set compute/zone europe-west1-b

 Compute Engine API を有効にする
gcloud services enable compute.googleapis.com

gsutil mb gs://fancy-store-$DEVSHELL_PROJECT_ID




gcloud compute instances create backend \
    --machine-type=e2-medium \
    --tags=backend \
   --metadata=startup-script-url=https://storage.googleapis.com/fancy-store-$DEVSHELL_PROJECT_ID/startup-script.sh

gcloud compute instances list

NAME: backend
ZONE: europe-west1-b
MACHINE_TYPE: e2-medium
PREEMPTIBLE: 
INTERNAL_IP: 10.132.0.4
EXTERNAL_IP: 34.79.121.173
STATUS: RUNNING


gcloud compute instances create frontend \
    --machine-type=e2-medium \
    --tags=frontend \
    --metadata=startup-script-url=https://storage.googleapis.com/fancy-store-$DEVSHELL_PROJECT_ID/startup-script.sh

NAME: frontend
ZONE: europe-west1-b
MACHINE_TYPE: e2-medium
PREEMPTIBLE: 
INTERNAL_IP: 10.132.0.5
EXTERNAL_IP: 34.14.109.132
STATUS: RUNNING


firewall
gcloud compute firewall-rules create fw-fe \
    --allow tcp:8080 \
    --target-tags=frontend

gcloud compute firewall-rules create fw-be \
    --allow tcp:8081-8082 \
    --target-tags=backend


watch -n 2 curl http://34.14.109.132:8080

watch -n 2 curl http://34.14.109.132:8080/api/health



gcloud compute instances stop frontend
gcloud compute instances stop backend
gcloud compute instance-templates create fancy-fe \
    --source-instance=frontend
gcloud compute instance-templates create fancy-be \
    --source-instance=backend
gcloud compute instance-templates list


マネージド インスタンス グループを作成する

gcloud compute instance-groups managed create fancy-fe-mig \
    --base-instance-name fancy-fe \
    --size 2 \
    --template fancy-fe

gcloud compute instance-groups managed create fancy-be-mig \
    --base-instance-name fancy-be \
    --size 2 \
    --template fancy-be

これらのマネージド インスタンス グループではインスタンス テンプレートを使用して、各グループ内で 2 つのインスタンスが起動するように構成します。インタンスには自動で名前が付けられ、base-instance-name で指定した名前の後にランダムな文字が付いたものになります。
NAME: fancy-fe-mig
LOCATION: europe-west1-b
SCOPE: zone
BASE_INSTANCE_NAME: fancy-fe
SIZE: 0
TARGET_SIZE: 2
INSTANCE_TEMPLATE: fancy-fe
AUTOSCALED: no


gcloud compute instance-groups set-named-ports fancy-fe-mig \
    --named-ports frontend:8080
gcloud compute instance-groups set-named-ports fancy-be-mig \
    --named-ports orders:8081,products:8082

frontend 用と backend 用の両方のヘルスチェックを作成し、3 回連続して Unhealthy（異常）のステータスが返った場合は修復を行うようにします。
gcloud compute health-checks create http fancy-fe-hc \
    --port 8080 \
    --check-interval 30s \
    --healthy-threshold 1 \
    --timeout 10s \
    --unhealthy-threshold 3
gcloud compute health-checks create http fancy-be-hc \
    --port 8081 \
    --request-path=/api/orders \
    --check-interval 30s \
    --healthy-threshold 1 \
    --timeout 10s \
    --unhealthy-threshold 3

ヘルスチェックのプローブがポート 8080、8081 のマイクロサービスに接続できるようにファイアウォール ルールを作成します。
gcloud compute firewall-rules create allow-health-check \
    --allow tcp:8080-8081 \
    --source-ranges 130.211.0.0/22,35.191.0.0/16 \
    --network default

ヘルスチェックを各サービスに適用します。
gcloud compute instance-groups managed update fancy-fe-mig \
    --health-check fancy-fe-hc \
    --initial-delay 300
gcloud compute instance-groups managed update fancy-be-mig \
    --health-check fancy-be-hc \
    --initial-delay 300


HTTP(S) ロードバランサを作成する

各サービスのトラフィックを処理できるインスタンスを判断するためのヘルスチェックを作成します
gcloud compute http-health-checks create fancy-fe-frontend-hc \
  --request-path / \
  --port 8080
gcloud compute http-health-checks create fancy-be-orders-hc \
  --request-path /api/orders \
  --port 8081
gcloud compute http-health-checks create fancy-be-products-hc \
  --request-path /api/products \
  --port 8082
これらは、ロードバランサ用のヘルスチェックであり、ロードバランサからのトラフィック転送のみを処理します。これにより、マネージド インスタンス グループがインスタンスを再作成することはありません。


ロードバランスされたトラフィックの送信先となるバックエンド サービスを作成します。バックエンド サービスでは、先ほど作成したヘルスチェックと名前付きポートを使用します。
gcloud compute backend-services create fancy-fe-frontend \
  --http-health-checks fancy-fe-frontend-hc \
  --port-name frontend \
  --global
gcloud compute backend-services create fancy-be-orders \
  --http-health-checks fancy-be-orders-hc \
  --port-name orders \
  --global
gcloud compute backend-services create fancy-be-products \
  --http-health-checks fancy-be-products-hc \
  --port-name products \
  --global

ロードバランサのバックエンド サービスを追加します。
gcloud compute backend-services add-backend fancy-fe-frontend \
  --instance-group fancy-fe-mig \
  --instance-group-zone europe-west1-b \
  --global
gcloud compute backend-services add-backend fancy-be-orders \
  --instance-group fancy-be-mig \
  --instance-group-zone europe-west1-b \
  --global
gcloud compute backend-services add-backend fancy-be-products \
  --instance-group fancy-be-mig \
  --instance-group-zone europe-west1-b \
  --global

URL マップを作成します。URL マップは、どの URL をどのバックエンド サービスに転送するのかを決めるものです。
gcloud compute url-maps create fancy-map \
  --default-service fancy-fe-frontend

パスマッチャーを作成して /api/orders と /api/products のパスを、それぞれのサービスに転送するようにします。
gcloud compute url-maps add-path-matcher fancy-map \
   --default-service fancy-fe-frontend \
   --path-matcher-name orders \
   --path-rules "/api/orders=fancy-be-orders,/api/products=fancy-be-products"
  

URL マップに関連付けるプロキシを作成します。
gcloud compute target-http-proxies create fancy-proxy \
  --url-map fancy-map

パブリック IP アドレスとポートをプロキシに関連付けるグローバル転送ルールを作成します。
gcloud compute forwarding-rules create fancy-http-rule \
  --global \
  --target-http-proxy fancy-proxy \
  --ports 80


ロードバランサのIPアドレス
gcloud compute forwarding-rules list --global

NAME: fancy-http-rule
REGION: 
IP_ADDRESS: 34.149.201.25
IP_PROTOCOL: TCP
TARGET: fancy-proxy


フロントエンドインスタンス更新
gcloud compute instance-groups managed rolling-action replace fancy-fe-mig \
    --max-unavailable 100%


CDN
gcloud compute backend-services update fancy-fe-frontend \
    --enable-cdn --global



gcloud compute instance-templates create fancy-fe-new \
    --source-instance=frontend \
    --source-instance-zone=europe-west1-b



gcloud compute instance-templates create fancy-fe-new \
    --source-instance=frontend \
    --source-instance-zone=europe-west1-c
</ql-code-block 

5. 新しいインスタンス テンプレートをマネージド インスタンス グループに展開します。

```bash
gcloud compute instance-groups managed rolling-action start-update fancy-fe-mig \
    --version template=fancy-fe-new
```

6. 30 秒待ってから、次のコマンドを実行して更新のステータスをモニタリングします。

```bash
watch -n 2 gcloud compute instance-groups managed list-instances fancy-fe-mig
```

このコマンドが完了するまでに少し時間がかかります。

次の状態のインスタンスが 1 つ以上あることを確認します。

* STATUS: __RUNNING__
* ACTION __None__ に設定
* INSTANCE\_TEMPLATE: 新しいテンプレートの名前（fancy-fe-new）

7. リストにあるマシン名の一つを__コピー__して次のコマンドで使用します。8. Ctrl+C キーを押して「watch」プロセスを終了します。9. 次のコマンドを実行して、仮想マシンが新しいマシンタイプ（custom-4-3840）を使用していることを確認します。\[VM\_NAME\] は新しく作成されたインスタンス名に置き換えます。
