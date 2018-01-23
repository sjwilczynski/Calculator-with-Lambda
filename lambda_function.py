def lambda_handler(event, context):
    
    params = event["queryStringParameters"]
    operation = event['pathParameters']['op']
    if operation == 'dodawanie':
        body = int(params['a']) + int(params['b'])
    
    reponse = { "statusCode": 200,
        "headers": {
            "my_header": "Do i need this header?r"
        },
        "body" : body,
        "isBase64Encoded": False
    }
    return reponse
