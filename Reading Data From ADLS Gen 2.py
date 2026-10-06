# Databricks notebook source
print('Hello Databricks')

# COMMAND ----------

dbutils.fs.ls('abfss://datalake@dacstorage.dfs.core.windows.net/practice')

# COMMAND ----------

df=spark.read.format('csv').option('header','true').load('abfss://datalake@dacstorage.dfs.core.windows.net/practice/sales.csv - Sheet1.csv')

# COMMAND ----------

df.show()

# COMMAND ----------

