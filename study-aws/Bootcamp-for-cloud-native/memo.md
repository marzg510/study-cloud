# 実践力を鍛えるBootcamp - クラウドネイティブ編 -

## Architecture

https://static.us-east-1.prod.workshops.aws/public/18ca5392-a44d-40f2-aea3-939f4ee95f33/static/Architecture.png

## Step 1

VS Code Server

### Commands

aws --version


AWS_REGION="ap-northeast-1"
aws configure set region ${AWS_REGION}
aws configure get region

IAMのステータス確認
aws sts get-caller-identity

