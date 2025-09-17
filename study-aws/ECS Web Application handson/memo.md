ECS Web Application ハンズオン
https://catalog.workshops.aws/ecs-web-application-handson/ja-JP

AWS Console
https://ap-northeast-1.console.aws.amazon.com/console/home?region=ap-northeast-1#

## 設定

ユーザー名
masaru

VSCode　password

イメージURI
246262167857.dkr.ecr.ap-northeast-1.amazonaws.com/rails-app


ELB DNS名
ecs-ec2-alb-742525670.ap-northeast-1.elb.amazonaws.com
ecs-fargate-alb-351239520.ap-northeast-1.elb.amazonaws.com



## コマンド群

docker build -t rails-app .
-t コンテナイメージの名前

docker image ls
images

### プッシュコマンド

aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 246262167857.dkr.ecr.ap-northeast-1.amazonaws.com
docker build -t rails-app .
docker tag rails-app:latest 246262167857.dkr.ecr.ap-northeast-1.amazonaws.com/rails-app:latest
docker push 246262167857.dkr.ecr.ap-northeast-1.amazonaws.com/rails-app:latest


## 用語

タスク	ECS でコンテナを実行する際の最小の実行単位であり、1 つのタスクには 1 つ以上のコンテナを含むことができます。
タスク定義	コンテナイメージやリソース量などを設定したテンプレートで、タスク定義をもとにタスクを起動します。
サービス	タスクを "複数" 実行 "し続ける" ように設定したり、ALB との連携を設定したりできます。

https://static.us-east-1.prod.workshops.aws/public/e28ff713-a922-450b-9611-a7ca046304f8/static/images_optimized/ecs/task/1.png


## エラーなど

ecs-ec2-service のデプロイ中にエラーが発生しました
Resource handler returned message: "The following Availability Zones ap-northeast-1a cannot be associated with a load balancer. Please try a different Availability Zone. (Service: ElasticLoadBalancingV2, Status Code: 400, Request ID: c1eba965-0ab7-4ce0-867c-ddb4cad5ddc9) (SDK Attempt Count: 1)" (RequestToken: 2413177a-1d6f-e6f4-5983-dd01d675da86, HandlerErrorCode: InvalidRequest)

CloudFormationのスタックをロールバック
クラスターを削除

## [hey](https://github.com/rakyll/hey)  

リクエスト発生ツール
(hey is a tiny program that sends some load to a web application.)

インストール
wget https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_amd64
chmod +x hey_linux_amd64
sudo mv hey_linux_amd64 /usr/local/bin/hey

負荷発生コマンド
FARGATE_ALB_NAME=ecs-fargate-alb
FARGATE_ALB_DNS=$(aws elbv2 describe-load-balancers --name ${FARGATE_ALB_NAME} --query "LoadBalancers[].DNSName" --output text)
hey -c 10 -z 10m http://${FARGATE_ALB_DNS}
