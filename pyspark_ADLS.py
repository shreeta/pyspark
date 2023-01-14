# Databricks notebook source
containerName = "blobpyspark"
storageAccountName = "pyspark007"
sas = "?sv=2021-06-08&ss=bfqt&srt=c&sp=rwdlacupyx&se=2023-01-15T00:32:25Z&st=2023-01-14T16:32:25Z&spr=https&sig=Tw8ajqKTNoPbboVJsXzzSOcqKhR2QyubPtBaxevY8tU%3D"
config = "fs.azure.sas." + containerName+ "." + storageAccountName + ".blob.core.windows.net"

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://azsqlshackcontainer@azsqlshackstorage.blob.core.windows.net/1000 Sales Records.csv",
  mountPoint = "/mnt/myfile",
  extraConfigs = Map(config -> sas))

spark.read.load("abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<path-to-data>")

