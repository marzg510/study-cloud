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

### Challenge 2 Lambda

#### 参考
https://qiita.com/hanzawak/items/0b0e3bc54653e2d3c734

### cliサンプル

#### 実行ロール作成
```
aws iam create-role --role-name execute-lambda-for-study-cn \
 --assume-role-policy-document \
'{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

出力
```JSON
{
    "Role": {
        "Path": "/",
        "RoleName": "execute-lambda-for-study-cn",
        "RoleId": "AROATSVS6PEY2LY6DMQW3",
        "Arn": "arn:aws:iam::246262167857:role/execute-lambda-for-study-cn",
        "CreateDate": "2025-10-26T05:42:35+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
    }
}
```

#### ロールにポリシーをアタッチ

Cloud Watchにログを書くポリシーをアタッチ

```bash
aws iam attach-role-policy --role-name execute-lambda-for-study-cn \
 --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

出力：なし

#### デプロイパッケージを作成

```
zip lambda_test.zip lambda_test.py
```

#### Lambda関数を作成

```bash
aws lambda create-function --function-name lambda_test_for_study_cn \
--zip-file fileb://lambda_test.zip --handler lambda_test.lambda_handler --runtime python3.13 \
--role arn:aws:iam::246262167857:role/execute-lambda-for-study-cn
```

出力
```JSON
{
    "FunctionName": "lambda_test_for_study_cn",
    "FunctionArn": "arn:aws:lambda:ap-northeast-1:246262167857:function:lambda_test_for_study_cn",
    "Runtime": "python3.13",
    "Role": "arn:aws:iam::246262167857:role/execute-lambda-for-study-cn",
    "Handler": "lambda_test.lambda_handler",
    "CodeSize": 316,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2025-10-26T05:53:18.900+0000",
    "CodeSha256": "cO0DJfuDM2HQqJe2iVstBfd0qBM52PaH8URAnE57130=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "6fda0a5b-a323-43da-a3ae-d79885bdd20b",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    "PackageType": "Zip",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    },
    "RuntimeVersionConfig": {
        "RuntimeVersionArn": "arn:aws:lambda:ap-northeast-1::runtime:fe7a78198cc1037d599c8e576c9b94c4d6b88f8067b86f7d3481b75d9fd76c24"
    },
    "LoggingConfig": {
        "LogFormat": "Text",
        "LogGroup": "/aws/lambda/lambda_test_for_study_cn"
    }
}
```

#### DynamoDBへの書き込みfunctionのCLIによる作成

#### 実行ロール作成
```bash
aws iam create-role --role-name execute-lambda-for-study-cn \
 --assume-role-policy-document \
'{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

出力
```JSON
```

##### DynamoDBへの書き込みポリシーをロールに追加

```bash
aws iam put-role-policy --role-name execute-lambda-for-study-cn \
  --policy-name access-dynamodb-for-study-cn \
  --policy-document file://dynamodb-policy.json
```JSON

出力：なし

#### デプロイパッケージを作成

```
zip write_db.zip write_db.py
```

#### Lambda関数を作成

```bash
aws lambda create-function --function-name write_db_for_study_cn \
--zip-file fileb://write_db.zip --handler write_db.lambda_handler --runtime python3.13 \
--role arn:aws:iam::246262167857:role/execute-lambda-for-study-cn
```

出力
```JSON
{
    "FunctionName": "write_db_for_study_cn",
    "FunctionArn": "arn:aws:lambda:ap-northeast-1:246262167857:function:write_db_for_study_cn",
    "Runtime": "python3.13",
    "Role": "arn:aws:iam::246262167857:role/execute-lambda-for-study-cn",
    "Handler": "write_db.lambda_handler",
    "CodeSize": 809,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2025-10-26T07:56:01.070+0000",
    "CodeSha256": "X7ZkJlWtrfgmX20hq/Pq/r4qBWkYoX7ftKe0xPY9X4E=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "8751c1c9-1fb6-4b47-b800-65ca7a5b50f0",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    "PackageType": "Zip",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    },
    "RuntimeVersionConfig": {
        "RuntimeVersionArn": "arn:aws:lambda:ap-northeast-1::runtime:fe7a78198cc1037d599c8e576c9b94c4d6b88f8067b86f7d3481b75d9fd76c24"
    },
    "LoggingConfig": {
        "LogFormat": "Text",
        "LogGroup": "/aws/lambda/write_db_for_study_cn"
    }
}
```

#### テスト

イベントJSON(WriteDBTest) body部分のみ
```JSON
  "body": "{\"training\": \"トレーニング名\", \"email\": \"メールアドレス\", \"name\": \"申込者氏名\",\"company\": \"会社名\"}",
```





### Commands

aws --version


AWS_REGION="ap-northeast-1"
aws configure set region ${AWS_REGION}
aws configure get region

IAMのステータス確認
aws sts get-caller-identity

