import findspark
findspark.init()
from pyspark.sql import *
from src.main.utility.logging_config import *

def spark_session():
    spark = SparkSession.builder.master("local[*]") \
        .appName("lokesh_spark2")\
        .getOrCreate()
    logger.info("spark session %s",spark)
    return spark

