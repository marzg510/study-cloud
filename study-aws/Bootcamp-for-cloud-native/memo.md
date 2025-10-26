# 実践力を鍛えるBootcamp - クラウドネイティブ編 -

https://catalog.us-east-1.prod.workshops.aws/workshops/a9b0eefd-f429-4859-9881-ce3a7f1a4e5f

## Architecture

![Architecture](https://static.us-east-1.prod.workshops.aws/public/18ca5392-a44d-40f2-aea3-939f4ee95f33/static/Architecture.png)

## Env

- AWS CLI .
- AWS Cloud Development Kit (CDK) .
- AWS SAM CLI .
- AWS Q Developer for VSCode .
- Git .
- Docker .
- Python 3.13 .
- Amazon Corretto OpenJDK .
- Typescript .
- Node .
- Vite .
- Go .
- Rust .

### docker

CLI
https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-docker.html

``` bash
docker run --rm -it public.ecr.aws/aws-cli/aws-cli command
```

## Step 1

### Challenge 3

#### CloudFront

Cloud frontを前に置いたサイト
https://d3ic2f7g0k54la.cloudfront.net/index.html

デフォルトルートオブジェクトを設定後
https://d3ic2f7g0k54la.cloudfront.net/

CloudFront経由でS3の静的Webサイトを公開する手順
https://dev.classmethod.jp/articles/cloudfront-s3web/

今のコンソールだと、CloudFrontのディストリビューションの作成から、
OAC作成を自動でやってくれる。
デフォルトルートオブジェクトを設定しないと、index.htmlを省略できない。
（S3はデフォルトでできていた）

## Step 2

- [Step2](https://catalog.us-east-1.prod.workshops.aws/workshops/a9b0eefd-f429-4859-9881-ce3a7f1a4e5f/ja-JP/step2-serverless)

アーキテクチャ
![arch](https://static.us-east-1.prod.workshops.aws/public/18ca5392-a44d-40f2-aea3-939f4ee95f33/static/Step2/Step2_Architecture.png)


### Commands

aws --version


AWS_REGION="ap-northeast-1"
aws configure set region ${AWS_REGION}
aws configure get region

IAMのステータス確認
aws sts get-caller-identity

