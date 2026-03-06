import boto3
import os
bucket_name = "decapstone-bucket"
file_path = r"C:\Users\Hanifa Fatma\Desktop\python\my_project\data\cleaned_data.parquet"
s3_key = "raw/cleaned_data.parquet"
s3 = boto3.client("s3")
s3.upload_file(file_path, bucket_name,s3_key)
print("uploaded successfully")