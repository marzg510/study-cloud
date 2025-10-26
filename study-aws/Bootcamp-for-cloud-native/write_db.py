import json
import boto3
from decimal import Decimal

ddb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    print(event)
    # Eventから送信されてきた body のデータを読み取ります
    body = json.loads(event["body"])

    # body に入っているデータを取り出し、DynamoDBへのデータ登録のために設定します。
    params = {
        'TableName': 'TrainingApplicant',
        'Item': {
            'training': {'S': body['training']},
            'email': {'S': body['email']},
            'name': {'S': body['name']},
            'company': {'S': body['company']}
        }
    }

    # DynamoDB Document Client を使ってデータを登録(Put)します。
    try:
        # データが正常に登録できたら、 Status Code に 201 を返します。
        data = ddb_client.put_item(**params)
        response = {
            'statusCode': 201,
            'body': json.dumps(data)
        }
    except Exception as err:
        # エラーが発生したらエラーログを出力し、Status Codeに 500 を返します。
        print('Error', err)
        response = {
            'statusCode': 500,
            'body': str(err)
        }
    
    return response