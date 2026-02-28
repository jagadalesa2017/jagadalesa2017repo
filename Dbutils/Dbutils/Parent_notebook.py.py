# Databricks notebook source
# MAGIC %md
# MAGIC # Parent notebook
# MAGIC

# COMMAND ----------

# MAGIC %run ./Utils

# COMMAND ----------

print(a)

# COMMAND ----------

# DBTITLE 1,Cell 3
sum(2,4)

# COMMAND ----------

# dbutls.notebook.run used to run whole notebook but %run is used to run to import notebook and we can run any function as per demand in this notebook like here imported Utils notebook and accessing any function declared in Utils notebook.
# result=dbutils.notebook.run("Child_Notebook.py",60)
# print("Result from child notebook is :{0}".format(result))

# COMMAND ----------

result=dbutils.notebook.run("Child_notebook_1",60,{'region':'WEST'})
print("Result from child notebook is :{0}".format(result))

# COMMAND ----------

# DBTITLE 1,Cell 4
from datetime import datetime

Parameter = {

    "region": "INDIA",
    "run_date": datetime.now().isoformat()
}
result = dbutils.notebook.run(
    "Child_notebook_1",
    120,
    Parameter
)

print("Result from child notebook is: ".format(result))
