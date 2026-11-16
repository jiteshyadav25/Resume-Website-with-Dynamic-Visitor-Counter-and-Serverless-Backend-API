
import json
import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("CloudResumeCounter")


def lambda_handler(event, context):

    try:
        response = table.update_item(
            Key={
                "id": "resume"
            },
            UpdateExpression="ADD visits :increment",
            ExpressionAttributeValues={
                ":increment": 1
            },
            ReturnValues="UPDATED_NEW"
        )

        visitor_count = int(response["Attributes"]["visits"])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "visits": visitor_count
            })
        }

    except Exception as error:

        print("Error:", str(error))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Unable to update visitor count"
            })
        }
