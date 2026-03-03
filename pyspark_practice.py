import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window 
spark = SparkSession.builder.appName("Pyspark_practice").getOrCreate()
df = spark.read.csv("data/cleaned_data.csv", header = True, inferSchema = True)
df.show() 
#df1 = df["Payment Method"]     it will return a column not a dataframe and window function is applicable on dataframes only

window = Window.partitionBy("Payment Method")
df1 = df.withColumn("Total Sale per payment method", F.sum("Total Spent").over(window)) 
df1.show()

df1 = df.groupBy("Item").agg(F.sum("Total Spent").alias("Total sale per item")).orderBy(F.desc("Total sale per item"))
df1.show(5)

df1 = df.groupBy("Item").agg(F.sum("Quantity").alias("Total Quantity per item")).orderBy(F.desc("Total Quantity per item"))
df1.show()

item_price_per_unit = df.groupBy("Item").agg(F.avg("Price Per Unit").alias("item_prices_per_unit")).orderBy(F.desc("item_prices_per_unit"))
item_price_per_unit.show()

df1 = df.groupBy("Location").agg(F.sum("Total Spent").alias("Total spent per location")).orderBy(F.desc("total spent per location"))
df1.show()

df1 = df.orderBy(F.desc("Transaction Date"))
df1.show()

df1 = df.orderBy(F.desc("Total Spent")).select("Transaction Date", "Total Spent")
df1.show()

df1 = df.groupBy("Item").agg(F.avg("Total Spent").alias("average sale")).orderBy(F.desc("average sale"))
df1.show()

df1 = df.where(df["Item"] == "Coffee")
df1.show()