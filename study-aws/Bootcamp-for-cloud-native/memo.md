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

pythonイメージからインストール

```
docker compose up -d
docker compose exec -it aws-cli bash
```


参考：CLI
https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-docker.html

``` bash
docker run --rm -it public.ecr.aws/aws-cli/aws-cli command
```

参考：AWS CLI v2 をdockerで使えるようにする
https://zenn.dev/tokku5552/articles/aws-container

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

### Challenge 1

DynamoDB table

```
aws dynamodb create-table \
    --table-name TrainingApplicant \
    --attribute-definitions \
        AttributeName=training,AttributeType=S \
        AttributeName=email,AttributeType=S \
    --key-schema AttributeName=training,KeyType=HASH AttributeName=email,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --table-class STANDARD
```

出力
```
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "email",
                "AttributeType": "S"
            },
            {
                "AttributeName": "training",
                "AttributeType": "S"
            }
        ],
        "TableName": "TrainingApplicant",
        "KeySchema": [
            {
                "AttributeName": "training",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "email",
                "KeyType": "RANGE"
            }
        ],
        "TableStatus": "CREATING",
        "CreationDateTime": "2025-10-26T05:17:06.415000+00:00",
        "ProvisionedThroughput": {
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 0,
            "WriteCapacityUnits": 0
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:ap-northeast-1:246262167857:table/TrainingApplicant",
        "TableId": "7fffea0c-758f-432f-8c0b-4edc468e4713",
        "BillingModeSummary": {
            "BillingMode": "PAY_PER_REQUEST"
        },
        "TableClassSummary": {
            "TableClass": "STANDARD"
        },
        "DeletionProtectionEnabled": false
    }
}
```

### Commands

aws --version


AWS_REGION="ap-northeast-1"
aws configure set region ${AWS_REGION}
aws configure get region

IAMのステータス確認
aws sts get-caller-identity

