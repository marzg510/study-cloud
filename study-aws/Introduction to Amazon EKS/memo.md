# EKS handson

## Commands

aws --version


AWS_REGION="ap-northeast-1"
aws configure set region ${AWS_REGION}
aws configure get region

IAMのステータス確認
aws sts get-caller-identity

### eksctl

インストール

curl -L "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin



eksctl version
0.214.0

kubectlのインストール

sudo curl -L -o /usr/local/bin/kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/0.214.0/2024-05-12/bin/linux/amd64/kubectl
sudo chmod +x /usr/local/bin/kubectl

# Kubernetes 1.31用（推奨）
sudo curl -L -o /usr/local/bin/kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.0/2024-09-12/bin/linux/amd64/kubectl
sudo chmod +x /usr/local/bin/kubectl


sudo rm /usr/local/bin/kubectl

kubectl version --client


eksクラスター作成

AWS_REGION=$(aws configure get region)
eksctl create cluster \
  --name=ekshandson \
  --version 1.31 \
  --nodes=3 --managed \
  --region ${AWS_REGION} --zones ${AWS_REGION}b,${AWS_REGION}c

ツールのインストール
  sudo yum -y install jq bash-completion tree gettext

kubectlコマンドの補完
kubectl completion bash > kubectl_completion
sudo mv kubectl_completion /etc/bash_completion.d/kubectl

docker コマンドの補完
sudo curl -L -o /etc/bash_completion.d/docker https://raw.githubusercontent.com/docker/cli/master/contrib/completion/bash/docker



eksctl get cluster

kubectl cluster-info

kubectl get node
NAME                                               STATUS   ROLES    AGE   VERSION
ip-192-168-2-44.ap-northeast-1.compute.internal    Ready    <none>   19m   v1.31.12-eks-99d6cc0
ip-192-168-34-13.ap-northeast-1.compute.internal   Ready    <none>   19m   v1.31.12-eks-99d6cc0
ip-192-168-58-48.ap-northeast-1.compute.internal   Ready    <none>   19m   v1.31.12-eks-99d6cc0

(⎈|i-040ac7d0c7f4b78eb@ekshandson:kube-system) masaru:~/environment $ kubectl get pod -n kube-system -o wide
NAME                             READY   STATUS    RESTARTS   AGE   IP               NODE                                               NOMINATED NODE   READINESS GATES
aws-node-cqllk                   2/2     Running   0          18m   192.168.2.44     ip-192-168-2-44.ap-northeast-1.compute.internal    <none>           <none>
aws-node-dw66c                   2/2     Running   0          18m   192.168.58.48    ip-192-168-58-48.ap-northeast-1.compute.internal   <none>           <none>
aws-node-mc94s                   2/2     Running   0          18m   192.168.34.13    ip-192-168-34-13.ap-northeast-1.compute.internal   <none>           <none>
coredns-5f486bd4cc-bb8sn         1/1     Running   0          19m   192.168.24.155   ip-192-168-2-44.ap-northeast-1.compute.internal    <none>           <none>
coredns-5f486bd4cc-k22qt         1/1     Running   0          19m   192.168.63.212   ip-192-168-58-48.ap-northeast-1.compute.internal   <none>           <none>
kube-proxy-cwm9w                 1/1     Running   0          18m   192.168.2.44     ip-192-168-2-44.ap-northeast-1.compute.internal    <none>           <none>
kube-proxy-kkgxt                 1/1     Running   0          18m   192.168.34.13    ip-192-168-34-13.ap-northeast-1.compute.internal   <none>           <none>
kube-proxy-l5wkl                 1/1     Running   0          18m   192.168.58.48    ip-192-168-58-48.ap-northeast-1.compute.internal   <none>           <none>
metrics-server-6d8c5d747-4znb9   1/1     Running   0          19m   192.168.4.42     ip-192-168-2-44.ap-northeast-1.compute.internal    <none>           <none>
metrics-server-6d8c5d747-rczfx   1/1     Running   0          19m   192.168.37.170   ip-192-168-34-13.ap-northeast-1.compute.internal   <none>           <none>

