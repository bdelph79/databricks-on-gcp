# Databricks notebook source
print("hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "hello world from SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC #Title
# MAGIC ## Title
# MAGIC ###Title 
# MAGIC * apple
# MAGIC * peach
# MAGIC * banana
# MAGIC 
# MAGIC 1. one
# MAGIC 2. two
# MAGIC 3. free

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()


# COMMAND ----------



# COMMAND ----------

dbutils.jobs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)
