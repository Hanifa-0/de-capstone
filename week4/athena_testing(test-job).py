import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import col

# Initialize Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# S3 paths
raw_path = "s3://decapstone-bucket/raw"
curated_path = "s3://decapstone-bucket/curated"

# Try reading from raw
try:
    df_raw = spark.read.csv(raw_path, header=True, inferSchema=True)
    print(f"Raw data read successfully, rows: {df_raw.count()}")
except Exception as e:
    print(f"Failed to read raw: {e}")

# Try writing to curated 
try:
    df_raw.limit(5).write.mode("overwrite").parquet(curated_path + "/permission_test")
    print("Write to curated succeeded!")
except Exception as e:
    print(f"Failed to write to curated: {e}")
