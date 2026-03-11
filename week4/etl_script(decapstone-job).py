import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import year, month, day, to_timestamp, col

# Job name
job_name = "decapstone-job"

# Initialize contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Glue job
job = Job(glueContext)
job.init(job_name, {})

# S3 paths
input_path = "s3://decapstone-bucket/raw"
output_path = "s3://decapstone-bucket/curated"

# Read CSV as Glue DynamicFrame
dynamic_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path]},
    format="csv",
    format_options={"withHeader": True, "inferSchema": True}
)

# Convert to Spark DataFrame
df = dynamic_df.toDF()

# Transform data
df_cleaned = df.withColumn("price per unit as int", col("Price Per Unit").cast("integer")) \
               .dropDuplicates() \
               .withColumn("timeForPartition", to_timestamp(col("Transaction Date"))) \
               .withColumn("year", year(col("Transaction Date"))) \
               .withColumn("month", month(col("Transaction Date"))) 
               

# Write partitioned Parquet
df_cleaned.write.mode("overwrite") \
          .partitionBy("year", "month") \
          .parquet(output_path)

# Commit job
job.commit()
