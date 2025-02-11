from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test CDE").getOrCreate()

users = [
    ("Mario", "Rossi",1),
    ("Luca", "Bianchi", 2),
    ("Marco", "Verdi",3)
         ]

usersColumn = ["firstname","lastname","id"]

usersDF = spark.createDataFrame(users, usersColumn)

usersDF.show()