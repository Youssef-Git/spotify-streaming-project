# Databricks notebook source
# MAGIC %pip install boto3
# MAGIC

# COMMAND ----------

from pyspark.sql.types import *

schema = StructType([
    StructField("event_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("track_id", StringType(), True),
    StructField("track_name", StringType(), True),
    StructField("artist_name", StringType(), True),
    StructField("genre", StringType(), True),
    StructField("duration_ms", LongType(), True),
    StructField("listened_ms", LongType(), True),
    StructField("timestamp", StringType(), True),
    StructField("platform", StringType(), True),
    StructField("country", StringType(), True)
])

df = spark.read.schema(schema).option("recursiveFileLookup", "true").json("/Volumes/workspace/bronze/spotify_events/events/")
df.display()

# COMMAND ----------

dbutils.fs.head("/Volumes/workspace/bronze/spotify_events/events/2026/07/13/19/0012e54c-00d5-4607-8aab-cabae6962744.json")

# COMMAND ----------

df.write \
  .format("delta") \
  .mode("overwrite") \
  .saveAsTable("workspace.bronze.spotify_events")

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP SCHEMA IF EXISTS workspace.silver_gold CASCADE;
# MAGIC DROP SCHEMA IF EXISTS workspace.silver_silver CASCADE;