import json
import boto3
from datetime import datetime
s3 = boto3.client('s3')
Bucket = "decapstone-bucket"

def lambda_handler(event, context):
    
        try:
            if isinstance(event.get('body'), str):
                payload = json.loads(event['body'])
            else:
                payload = event['body']  # already a dict
            
                print("successfully validated json")
        except Exception as e:
            return{
                'statusCode': 200,
                'body': json.dumps(f"invalid json:{e}")
            }
        data = payload.copy()
        received_at = datetime.utcnow().isoformat()
        data['received_at'] = received_at
        print(received_at)

        try:
            s3_key = f"staging/{received_at}.json"
            s3.put_object(
                Bucket = Bucket,
                Key = s3_key,
                Body = json.dumps(data)
        )

            return {
                'statusCode': 200,
                'body': json.dumps('success')
        }
        except Exception as e:
            return{
                'statusCode': 500,
                'body': json.dumps('failed uploading to s3')

        }
