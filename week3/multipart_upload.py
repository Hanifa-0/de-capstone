import boto3
from boto3.s3.transfer import TransferConfig
import os
bucket_name = "decapstone-bucket"
file_path = r"C:\Users\Hanifa Fatma\Desktop\python\my_project\data\cleaned_data.parquet"
s3_key = "raw/multipart.parquet"
s3 = boto3.client("s3")
config = TransferConfig(
    multipart_threshold=20,    #20 kb
    multipart_chunksize=20,    
    max_concurrency=1,
    use_threads=False
)

s3.upload_file(
    file_path,
    bucket_name,
    s3_key,
    Config=config
)

print("Multipart upload completed successfully")