import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import boto3
from pyspark.sql import functions as F
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
s3= boto3.client('s3')
job.init(args['JOB_NAME'], args)
input_file_path = "s3://new-dataset-bucket-create/raw/new_uncleaned.csv"
output_path ="s3://new-dataset-bucket-create/staging"
glue_dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type = "s3",
    connection_options={
        "paths":[input_file_path]
    },
    format="csv",
    format_options={
        "withHeader":True,
        "inferSchema":True,
        "separator":"|"
    }
    )
try:
    df = glue_dynamic_frame.toDF()
    print(df.columns)
except Exception as e:
    print(f"failed to convert to df: {e}")

df = df.dropDuplicates()
df= df.withColumn("Full_name", F.concat_ws(" ",F.col("First_Name"),F.col("Last_Name")))
df=  df.drop("First_Name", "Last_Name")
transformed_dynamic_frame = DynamicFrame.fromDF(df, glueContext, "transformed dynamic frame")
glueContext.write_dynamic_frame.from_options(
    frame =transformed_dynamic_frame,
    connection_type="s3",
    connection_options={
        "path" : output_path
    },
    format="parquet"
    )

job.commit()