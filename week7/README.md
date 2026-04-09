Step 1: upload an uncleaned dataset in s3 
![upload another uncleaned dataset in s3 ](images/uploaded_another_uncleaned_dataset_in_s3.png)

Step 2: Run Glue Crawler
![Run Glue Crawler](images/run_crawler.png)

Step 3: schema retrieved after running crawler
![schema created after running the crawler](images/schema_retrieved.png)

Step 4: create a glue job doing some transformation
![create glue job](images/glue_job.png)

Step 5: Run athena query on cleaned file in curated folder
![Run athena query on cleaned file in curated folder](images/running_athena_query_on_curated.png)

Step 6: athena query result
![athena query result](images/athena_query_result.png)

Step 7: Step function invoking lambda on success
![Step function invoking lambda on success](images/step_function_invoking_lambda.png)

Step 8: Step function invoking lambda on failure
![Step function invoking lambda on failure](images/step_function_invoking_lambda2.png)

