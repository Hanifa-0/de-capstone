import boto3
import json
from datetime import datetime
import base64
kinesis= boto3.client('kinesis', region_name = 'us-east-1')
bucket_name = "S3 bucket_name"
s3= boto3.client('s3')
def lambda_handler(event, context):
    batch_records={}
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        event_time_str = data['event_time']
        event_time = datetime.fromisoformat(event_time_str)
        partition = event_time.strftime('year=%Y/month=%m/day=%d/hour=%H')
        if partition not in batch_records:
            batch_records[partition]=[]
        batch_records[partition].append(data)
    for partition, records in batch_records.items():
        s3_key = f"raw/{partition}/{context.aws_request_id}.json"
        try:
            s3.put_object(
                Bucket= bucket_name,
                Key=s3_key,
                Body = json.dumps(records)
            )
        except Exception as e:
            print(f"Error:{e}")
