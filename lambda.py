def lambda_handler(event, context):
    print("hello world")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": "{\"message\": \"It's working!\"}"
    }