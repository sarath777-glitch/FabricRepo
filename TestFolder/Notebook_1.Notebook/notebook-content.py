# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "843f9bfb-a9e1-41f4-b3ba-c0e795960cfe",
# META       "default_lakehouse_name": "DevLakehouse",
# META       "default_lakehouse_workspace_id": "3dad38d0-7f3f-486e-9809-46377c147d77",
# META       "known_lakehouses": [
# META         {
# META           "id": "843f9bfb-a9e1-41f4-b3ba-c0e795960cfe"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/products.csv")
# df now is a Spark DataFrame containing CSV data from "Files/products.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

##Hi. This is for testing

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
