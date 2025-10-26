# 実践力を鍛えるBootcamp - クラウドネイティブ編 -

https://catalog.us-east-1.prod.workshops.aws/workshops/a9b0eefd-f429-4859-9881-ce3a7f1a4e5f

## Architecture

https://static.us-east-1.prod.workshops.aws/public/18ca5392-a44d-40f2-aea3-939f4ee95f33/static/Architecture.png

## Step 1

VS Code Server

http://20251024-marzg-step1.s3-website-ap-northeast-1.amazonaws.com


Challenge 3
CloudFront
https://d1a2i42g24e7ri.cloudfront.net

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


### Commands

aws --version


AWS_REGION="ap-northeast-1"
aws configure set region ${AWS_REGION}
aws configure get region

IAMのステータス確認
aws sts get-caller-identity

