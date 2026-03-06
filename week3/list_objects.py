import boto3
bucket_name = "decapstone-bucket"
s3 = boto3.client("s3")
response = s3.list_objects_v2(Bucket=bucket_name)

for obj in response["Contents"]:
    print(obj['Key'])
