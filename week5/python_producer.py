import boto3
import json
from datetime import datetime
kinesis = boto3.client('kinesis', region_name = 'us-east-1')
stream_name = "kinesis stream"
data = {
    "user_id": "12",
    "time": datetime.utcnow().isoformat()
}
def producer(data):
    json_str_data = json.dumps(data)
    try:
        kinesis.put_record(
            StreamName = stream_name,
            Data = json_str_data.encode('utf-8'),
            PartitionKey= data['user_id']
        )
    except Exception as e:
        print(f"error:{e}")
print(producer(data))