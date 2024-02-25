import shutil
import os
import findspark
from pyspark.sql import *
from src.main.utility.logging_config import *
from src.main.utility.spark_session import spark_session
from src.main.ProjectConfig import ProjectConfig,ProjectSchema
from pyspark.sql.functions import *
from pyspark.sql.types import *
from src.main.utility.s3_client_object import upload_file_to_s3


logger.info("**************creating spark session*****")
spark = spark_session()
logger.info("********spark session created *********")

def load_and_display_data(logger, spark, schema, config):
    try:
        logger.info(f"Loading data from {config} into DataFrame")
        data = spark.read.format('csv')\
            .schema(schema)\
            .option("header", True)\
            .load(config)
        # data.show()
        # data.printSchema()
        return data
    except Exception as e:
        logger.error(f"No file found at {config}")


def Seprate_csv_file_to_local(local_directory):
    try:
        logger.info("CSV file loading from transform data folder to another local folder for s3 ingestion")
        for main_dir,sub_dir,files in os.walk(ProjectConfig.local_directory):
            for file in files:
                if file.endswith(".csv"):
                    file_path = os.path.join(main_dir, file)
                    shutil.copy(file_path, ProjectConfig.destination_path)

    except Exception as e:
        logger.error(f"No file found {ProjectConfig.destination_path}")

Seprate_csv_file_to_local(ProjectConfig.local_directory)


#local_file_path,bucket_name,s3_file_key,aws_access_key, aws_secret_key

upload_file_to_s3(ProjectConfig.actualExpend_Vs_actualRequirement_Global_s3,ProjectConfig.bucket_name,"actualExpend_Vs_actualRequirement_Global_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.anualhealthexpenditure_Global_s3,ProjectConfig.bucket_name,"anualhealthexpenditure_Global_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.childLifeExpectancy_VS_health_Expend_Global_s3,ProjectConfig.bucket_name,"childLifeExpectancy_VS_health_Expend_Global_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.childMortVsHealthExpediture_Global_s3,ProjectConfig.bucket_name,"childMortVsHealthExpediture_Global_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.DevelopingCOE_TaxRevenue_VS_HC_Spending_s3,ProjectConfig.bucket_name,"DevelopingCOE_TaxRevenue_VS_HC_Spending_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.domesticSpendingPercentage_HC_GDP_s3,ProjectConfig.bucket_name,"domesticSpendingPercentage_HC_GDP_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.expenditureOn_NHS_UK_s3,ProjectConfig.bucket_name,"expenditureOn_NHS_UK_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.healthcareExpendVsGDP_Global_s3,ProjectConfig.bucket_name,"healthcareExpendVsGDP_Global_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.healthInsuranceCoverOn_US_s3,ProjectConfig.bucket_name,"healthInsuranceCoverOn_US_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.healthProtectionCover_Global_s3,ProjectConfig.bucket_name,"healthProtectionCover_Global_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.outOfPocketExpendOnHealth_s3,ProjectConfig.bucket_name,"outOfPocketExpendOnHealth_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.outOfPocketExpendOnHealth_VS_GDP_s3,ProjectConfig.bucket_name,"outOfPocketExpendOnHealth_VS_GDP_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.percentageWithoutHeathCover_US_s3,ProjectConfig.bucket_name,"percentageWithoutHeathCover_US_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.publicHealthInsuranceCoverage_s3,ProjectConfig.bucket_name,"publicHealthInsuranceCoverage_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.publicSpendingPercentage_HC_GDP_s3,ProjectConfig.bucket_name,"publicSpendingPercentage_HC_GDP_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.TotalExpendOn_HC_from_GDP_s3,ProjectConfig.bucket_name,"TotalExpendOn_HC_from_GDP_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)
upload_file_to_s3(ProjectConfig.TotalShareOfPublicExpenditure_HC_Global_s3,ProjectConfig.bucket_name,"TotalShareOfPublicExpenditure_HC_Global_s3",
                  ProjectConfig.aws_access_key,ProjectConfig.aws_secret_key)