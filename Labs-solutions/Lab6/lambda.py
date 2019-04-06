import boto3
import json
import os

region_name = 'eu-west-1'

print('Loading function')
dynamo = boto3.client('dynamodb',region_name, aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                      aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps(str(err) if err else res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }


def lambda_handler(event, context):
    operation = event['httpMethod']
    if operation == 'GET':
        return respond(None, dynamo.scan(**event['queryStringParameters']))
    elif operation == 'POST':
        return respond(None, dynamo.put_item(**json.loads(event['body'])))
    elif operation == 'DELETE':
        return respond(None, dynamo.delete_item(**json.loads(event['body'])))
    elif operation == 'PUT':
        return respond(None, dynamo.update_item(**json.loads(event['body'])))
    else:
        return respond(ValueError('Unsupported method %s' % operation))


print('--------------------GET event test')
get_event = {
    'httpMethod': 'GET',
    'queryStringParameters': {
        'TableName': 'shopping-list'
    }
}
print('--------------------REQUEST')
print(json.dumps(get_event, indent=2))

result = lambda_handler(get_event, None)
print('--------------------RESULT')
print(json.dumps(result, indent=2))
print('--------------------RESULT body')
print(json.dumps(json.loads(result['body']), indent=2))

print('--------------------POST event test')

myvar = {
    'TableName': 'shopping-list',
    'Item': {
        'ThingId': {
            'S': 'Red apples'
        }
    }
}

post_event = {
    'httpMethod': 'POST',
    'body': json.dumps(myvar, separators=(',', ':'))
}

print('--------------------REQUEST')
print(json.dumps(post_event, indent=2))


result = lambda_handler(post_event, None)

print('--------------------RESULT')
print(json.dumps(result, indent=2))
print('--------------------RESULT body')
print(json.dumps(json.loads(result['body']), indent=2))
