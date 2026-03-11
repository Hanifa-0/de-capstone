Step 1: Create a Glue database
![Create a Glue database](images/Glue_database.png)

Step 2: Create a Glue Crawler
![Create a Glue Crawler](images/glue_crawler.png)

Step 3: table created after running the crawler
![table created after running the crawler](images/table_created_after_running_crawler.png)

Step 4: Schema retrieved from the crawler
![Schema retrieved from the crawler](images/schema_from_glue_crawler.png)

Step 5: pyspark etl job
![pyspark etl job](images/decapstone_etl_job.png)

Step 6: etl job running
![etl job running](images/decapstone_etl_job_running.png)

Step 7: job bookmark enabled in ETL
![job bookmark enabled in ETL](images/decapstone_etl_job_bookmark_enabled.png)

Step 8: the result of the pyspark job is that the cleaned_data.csv file in raw folder of S3 is partitioned and saved in curated folder of S3 after partitioning on the basis of year and month of transaction date.
![the result of the pyspark job is that the cleaned_data.csv file in raw folder of S3 is partitioned and saved in curated folder of S3 after partitioning on the basis of year and month of transaction date.](images/partitioned_folders_created.png)

Step 9: Partitioned data in curated folder
![Partitioned data in curated folder](images/partitioned_folders_created_in_s3.png)

Step 10: Partitioned data
![Partitioned data](images/partitioned_folders_created_in_s3_.png)

Step 11: Create a crawler for partitioned data in curated folder in s3
![Create a crawler for partitioned data in curated folder in s3](images/crawler_for_partitioned_data_stored_in_curated.png)

Step 12: table created after running crawler
![table created after running crawler](images/table_created_for_partitioned_data.png)

Step 13: schema retrieved after running crawler
![schema retrieved after running crawler](images/schema_created_for_partitioned_data.png)

Step 14: In aws Data lake formation create an administrator using root account and register data location as raw and curated folders in s3
![In aws Data lake formation create an administrator using root account and register data location as raw and curated folders in s3](images/data_lake_locations.png)

Step 15: create an iam role with restricted permission for raw folder and full permission for curated folder
![create an iam role with restricted permission for raw folder and full permission for curated folder](images/glue_job_and_limited_user_permission.png)

Step 16: write the test glue job to check if iam user can access curated and not access raw
![write the test glue job to check if iam user can access curated and not access raw](images/test_job.png)

Step 17: login using iam user and write athena query for curated
![login using iam user and write athena query for curated](images/athena_query_for_curated.png)

Step 18: result for athena query
![result for athena query](images/result_of_athena_query_for_curated.png)

Step 19: result for athena query for raw (as raw folder was restricted for this user)
![result for athena query for raw (as raw folder was restricted for this user)](images/athena_query_for_raw.png)

Step 20: write CTAS query
![write CTAS query](images/CTAS_table.png)

Step 21: run time for query for partitioned data after using CTAS
![run time for query for partitioned data after using CTAS](images/result_after_using_ctas_query.png)

Step 22: run time for query for partitioned data before using CTAS
![run time for query for partitioned data before using CTAS](images/result_before_using_ctas_query.png)