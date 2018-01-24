from helper import process_request


def lambda_handler(event, context):
    params = event["queryStringParameters"]
    operation = event['pathParameters']['op']
    body = process_request(params, operation)
    response = {"statusCode": 200,
                "headers": {
                    "my_header": "Do i need this header?"
                },
                "body": body,
                "isBase64Encoded": False
                }
    return response
