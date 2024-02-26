import findspark
from pyspark.sql.functions import col
from pyspark.sql import *
from src.main.utility.logging_config import *
from src.main.utility.spark_session import spark_session
from src.main.ProjectConfig import ProjectConfig,ProjectSchema
from pyspark.sql.functions import *
from pyspark.sql.types import *
from src.main.PythonSparkJobs.DataIngestion import *
from src.main.utility.s3_client_object import upload_file_to_s3

# ***********cleaning the anualhealthexpenditure_Global data and loading into local*****************

def anualhealthexpenditure_Global():
    try:
        anualhealthexpenditure_Global = load_and_display_data(logger,spark,ProjectSchema.anualhealthexpenditure_Global_schema,
                                                              ProjectConfig.anualhealthexpenditure_Global)
        anualhealthexpenditure_Global = anualhealthexpenditure_Global.withColumnRenamed(
            "Indicator:Current health expenditure (CHE) per capita in PPP int$","Current_avg_HealthExpenditure_per_person")\
            .drop('Code')
        anualhealthexpenditure_Global = anualhealthexpenditure_Global.filter(~(col('Entity').contains('Low-income'))|
        (col('Entity').contains('Lower-middle-income')) | (col('Entity').contains('Upper-middle-income')) |((col('Entity').contains('High-income'))))
        anualhealthexpenditure_Global.show()
        logger.info("Dataframe anualhealthexpenditure_Global write into local")
        anualhealthexpenditure_Global.write.csv(f"{ProjectConfig.local_directory}/anualhealthexpenditure_Global", header=True, mode="overwrite")
        return anualhealthexpenditure_Global
    except Exception as e:
        logger.error("No file found")

anualhealthexpenditure_Global()

# cleaning the childMortVsHealthExpediture_Global data and loading into local

def childMortVsHealthExpediture_Global():
    try:
        childMortVsHealthExpediture_Global = load_and_display_data(logger,spark,ProjectSchema.childMortVsHealthExpediture_Global_schema,
                                                              ProjectConfig.childMortVsHealthExpediture_Global)
        childMortVsHealthExpediture_Global = childMortVsHealthExpediture_Global.filter(~(col('Year').contains('-10000')) |
          (col('Year').contains('-9000')) | (col('Year').contains('-8000')) | (col('Year').contains('-7000')) |(col('Year').contains('-6000'))|(col('Year').contains('-5000'))|(col('Year').contains('-3000')) |
          (col('Year').contains('-2000')) |(col('Year').contains('-1000')) |(col('Year').contains('0'))).drop('Code','Continent')
        childMortVsHealthExpediture_Global.show()
        childMortVsHealthExpediture_Global.write.csv(
            f"{ProjectConfig.local_directory}/childMortVsHealthExpediture_Global", header=True, mode="overwrite")
        return childMortVsHealthExpediture_Global
    except Exception as e:
        logger.error("No file found")

childMortVsHealthExpediture_Global()

# expenditureOn_NHS_UK does not have any ambiguity hence just loading to local

def expenditureOn_NHS_UK():
    try:
        expenditureOn_NHS_UK=load_and_display_data(logger, spark, ProjectSchema.expenditureOn_NHS_UK_schema,
                          ProjectConfig.expenditureOn_NHS_UK)
        expenditureOn_NHS_UK.show()
        expenditureOn_NHS_UK.write.csv(f"{ProjectConfig.local_directory}/expenditureOn_NHS_UK",header=True, mode="overwrite")
        return expenditureOn_NHS_UK
    except Exception as e:
        logger.error("No file found")

expenditureOn_NHS_UK()


# cleaning the healthcareExpendVsGDP_Global data and loading into local

def healthcareExpendVsGDP_Global():
    try:
        healthcareExpendVsGDP_Global=load_and_display_data(logger,spark,ProjectSchema.healthcareExpendVsGDP_Global_schema,
                                                ProjectConfig.healthcareExpendVsGDP_Global)
        healthcareExpendVsGDP_Global = healthcareExpendVsGDP_Global.drop('Continent').dropna()
        healthcareExpendVsGDP_Global.show()
        healthcareExpendVsGDP_Global.write.csv(f"{ProjectConfig.local_directory}/healthcareExpendVsGDP_Global", header=True, mode="overwrite")
        return healthcareExpendVsGDP_Global
    except Exception as e:
        logger.info("No file found")

healthcareExpendVsGDP_Global()


# No need to process healthInsuranceCoverOn_US data and loading into local

def healthInsuranceCoverOn_US():
    try:
        healthInsuranceCoverOn_US=load_and_display_data(logger, spark, ProjectSchema.healthInsuranceCoverOn_US_schema,
                          ProjectConfig.healthInsuranceCoverOn_US)
        healthInsuranceCoverOn_US.show()
        healthInsuranceCoverOn_US.write.csv(f"{ProjectConfig.local_directory}/healthInsuranceCoverOn_US",header=True, mode="overwrite")
        return healthInsuranceCoverOn_US
    except Exception as e:
        logger.error("No file found")

healthInsuranceCoverOn_US()

# No need to process healthProtectionCover_Global data and loading into local

def healthProtectionCover_Global():
    try:
        healthProtectionCover_Global=load_and_display_data(logger, spark, ProjectSchema.healthProtectionCover_Global_schema,
                          ProjectConfig.healthProtectionCover_Global)
        healthProtectionCover_Global.show()
        healthProtectionCover_Global.write.csv(f"{ProjectConfig.local_directory}/healthProtectionCover_Global",header=True, mode="overwrite")
        return healthProtectionCover_Global
    except Exception as e:
        logger.error("No file found")

healthProtectionCover_Global()

# cleaning the actualExpend_Vs_actualRequirement_Global data and loading into local

def actualExpend_Vs_actualRequirement_Global():
    try:
        actualExpend_Vs_actualRequirement_Global=load_and_display_data(logger,spark,ProjectSchema.actualExpend_Vs_actualRequirement_Global_schema,
                                                ProjectConfig.actualExpend_Vs_actualRequirement_Global)
        actualExpend_Vs_actualRequirement_Global = actualExpend_Vs_actualRequirement_Global.drop("Code", "Year",
                                                                                                "Continent")
        actualExpend_Vs_actualRequirement_Global.show()
        actualExpend_Vs_actualRequirement_Global.write.csv(f"{ProjectConfig.local_directory}/actualExpend_Vs_actualRequirement_Global",
                                               header=True, mode="overwrite")
        return actualExpend_Vs_actualRequirement_Global
    except Exception as e:
        logger.error("No file found")

actualExpend_Vs_actualRequirement_Global()


# cleaning the childLifeExpectancy_VS_health_Expend_Global data and loading into local
# filtering data based on year as per observation before 1960 almost all data is empty

def childLifeExpectancy_VS_health_Expend_Global():
    try:
        childLifeExpectancy_VS_health_Expend_Global=load_and_display_data(logger, spark, ProjectSchema.childLifeExpectancy_VS_health_Expend_Global_schema,
                          ProjectConfig.childLifeExpectancy_VS_health_Expend_Global)
        childLifeExpectancy_VS_health_Expend_Global = childLifeExpectancy_VS_health_Expend_Global.filter(
            col('Year') >= 1960)
        childLifeExpectancy_VS_health_Expend_Global = childLifeExpectancy_VS_health_Expend_Global.drop('Continent')
        childLifeExpectancy_VS_health_Expend_Global.show()
        childLifeExpectancy_VS_health_Expend_Global.write.csv(f"{ProjectConfig.local_directory}/childLifeExpectancy_VS_health_Expend_Global",header=True, mode="overwrite")
        return childLifeExpectancy_VS_health_Expend_Global
    except Exception as e:
        logger.error("No file found")

childLifeExpectancy_VS_health_Expend_Global()


# cleaning the percentageWithoutHeathCover_US data and loading into local

def percentageWithoutHeathCover_US():
    try:
        percentageWithoutHeathCover_US=load_and_display_data(logger, spark, ProjectSchema.percentageWithoutHeathCover_US_schema,
                          ProjectConfig.percentageWithoutHeathCover_US)
        percentageWithoutHeathCover_US=percentageWithoutHeathCover_US.drop("Code")
        percentageWithoutHeathCover_US.show()
        percentageWithoutHeathCover_US.write.csv(f"{ProjectConfig.local_directory}/percentageWithoutHeathCover_US",header=True, mode="overwrite")
        return percentageWithoutHeathCover_US
    except Exception as e:
        logger.error("No file found")

percentageWithoutHeathCover_US()

# cleaning the domesticSpendingPercentage_HC_GDP data and loading into local

def domesticSpendingPercentage_HC_GDP():
    try:
        domesticSpendingPercentage_HC_GDP=load_and_display_data(logger, spark, ProjectSchema.domesticSpendingPercentage_HC_GDP_schema,
                          ProjectConfig.domesticSpendingPercentage_HC_GDP)
        domesticSpendingPercentage_HC_GDP=domesticSpendingPercentage_HC_GDP.drop("Code")
        domesticSpendingPercentage_HC_GDP.show()
        domesticSpendingPercentage_HC_GDP.write.csv(f"{ProjectConfig.local_directory}/domesticSpendingPercentage_HC_GDP",header=True, mode="overwrite")
        return domesticSpendingPercentage_HC_GDP
    except Exception as e:
        logger.error("No file found")

domesticSpendingPercentage_HC_GDP()


# cleaning the publicSpendingPercentage_HC_GDP data and loading into local

def publicSpendingPercentage_HC_GDP():
    try:
        publicSpendingPercentage_HC_GDP=load_and_display_data(logger, spark, ProjectSchema.publicSpendingPercentage_HC_GDP_schema,
                          ProjectConfig.publicSpendingPercentage_HC_GDP)
        publicSpendingPercentage_HC_GDP=publicSpendingPercentage_HC_GDP.drop("Code")
        publicSpendingPercentage_HC_GDP.show()
        publicSpendingPercentage_HC_GDP.write.csv(f"{ProjectConfig.local_directory}/publicSpendingPercentage_HC_GDP",header=True, mode="overwrite")
        return publicSpendingPercentage_HC_GDP
    except Exception as e:
        logger.error("No file found")

publicSpendingPercentage_HC_GDP()


# cleaning the publicHealthInsuranceCoverage data and loading into local

def publicHealthInsuranceCoverage():
    try:
        publicHealthInsuranceCoverage=load_and_display_data(logger, spark, ProjectSchema.publicHealthInsuranceCoverage_schema,
                          ProjectConfig.publicHealthInsuranceCoverage)
        publicHealthInsuranceCoverage.show()
        publicHealthInsuranceCoverage.write.csv(f"{ProjectConfig.local_directory}/publicHealthInsuranceCoverage",header=True, mode="overwrite")
        return publicHealthInsuranceCoverage
    except Exception as e:
        logger.error("No file found")

publicHealthInsuranceCoverage()

# cleaning the outOfPocketExpendOnHealth data and loading into local

def outOfPocketExpendOnHealth():
    try:
        outOfPocketExpendOnHealth=load_and_display_data(logger, spark, ProjectSchema.outOfPocketExpendOnHealth_schema,
                          ProjectConfig.outOfPocketExpendOnHealth)
        outOfPocketExpendOnHealth = outOfPocketExpendOnHealth.drop('Code')
        outOfPocketExpendOnHealth.show()
        outOfPocketExpendOnHealth.write.csv(f"{ProjectConfig.local_directory}/outOfPocketExpendOnHealth",header=True, mode="overwrite")
        return outOfPocketExpendOnHealth
    except Exception as e:
        logger.error("No file found")

outOfPocketExpendOnHealth()



# cleaning the outOfPocketExpendOnHealth_VS_GDP data and loading into local
# After my observation I found before year 2000 all data is missing hence removing all and keeping after data
# additionaly we have population columns in other table hence removing that also

def outOfPocketExpendOnHealth_VS_GDP():
    try:
        outOfPocketExpendOnHealth_VS_GDP=load_and_display_data(logger, spark, ProjectSchema.outOfPocketExpendOnHealth_VS_GDP_schema,
                          ProjectConfig.outOfPocketExpendOnHealth_VS_GDP)
        outOfPocketExpendOnHealth_VS_GDP = outOfPocketExpendOnHealth_VS_GDP=outOfPocketExpendOnHealth_VS_GDP.filter(col('Year')>=2000)
        outOfPocketExpendOnHealth_VS_GDP = outOfPocketExpendOnHealth_VS_GDP.drop('Continent','Population (historical estimates)','Code')
        outOfPocketExpendOnHealth_VS_GDP.show()
        outOfPocketExpendOnHealth_VS_GDP.write.csv(f"{ProjectConfig.local_directory}/outOfPocketExpendOnHealth_VS_GDP",header=True, mode="overwrite")
        return outOfPocketExpendOnHealth_VS_GDP
    except Exception as e:
        logger.error("No file found")

outOfPocketExpendOnHealth_VS_GDP()



# cleaning the TotalShareOfPublicExpenditure_HC_Global data and loading into local

def TotalShareOfPublicExpenditure_HC_Global():
    try:
        TotalShareOfPublicExpenditure_HC_Global=load_and_display_data(logger, spark, ProjectSchema.TotalShareOfPublicExpenditure_HC_Global_schema,
                          ProjectConfig.TotalShareOfPublicExpenditure_HC_Global)
        TotalShareOfPublicExpenditure_HC_Global = TotalShareOfPublicExpenditure_HC_Global.drop("Code")
        TotalShareOfPublicExpenditure_HC_Global.show()
        TotalShareOfPublicExpenditure_HC_Global.write.csv(f"{ProjectConfig.local_directory}/TotalShareOfPublicExpenditure_HC_Global",header=True, mode="overwrite")
        return TotalShareOfPublicExpenditure_HC_Global
    except Exception as e:
        logger.error("No file found")

TotalShareOfPublicExpenditure_HC_Global()


# cleaning the TotalExpendOn_HC_from_GDP data and loading into local

def TotalExpendOn_HC_from_GDP():
    try:
        TotalExpendOn_HC_from_GDP=load_and_display_data(logger, spark, ProjectSchema.TotalExpendOn_HC_from_GDP_schema,
                          ProjectConfig.TotalExpendOn_HC_from_GDP)
        TotalExpendOn_HC_from_GDP = TotalExpendOn_HC_from_GDP.dropna()
        TotalExpendOn_HC_from_GDP.show()
        TotalExpendOn_HC_from_GDP.write.csv(f"{ProjectConfig.local_directory}/TotalExpendOn_HC_from_GDP",header=True, mode="overwrite")
        return TotalExpendOn_HC_from_GDP
    except Exception as e:
        logger.error("No file found")

TotalExpendOn_HC_from_GDP()

# cleaning the DevelopingCOE_TaxRevenue_VS_HC_Spending data and loading into local
# This table has almost all data null except 2014

def DevelopingCOE_TaxRevenue_VS_HC_Spending():
    try:
        DevelopingCOE_TaxRevenue_VS_HC_Spending=load_and_display_data(logger, spark, ProjectSchema.DevelopingCOE_TaxRevenue_VS_HC_Spending_schema,
                              ProjectConfig.DevelopingCOE_TaxRevenue_VS_HC_Spending)
        DevelopingCOE_TaxRevenue_VS_HC_Spending=DevelopingCOE_TaxRevenue_VS_HC_Spending.drop('Code')
        DevelopingCOE_TaxRevenue_VS_HC_Spending.show()
        DevelopingCOE_TaxRevenue_VS_HC_Spending.write.csv(f"{ProjectConfig.local_directory}/DevelopingCOE_TaxRevenue_VS_HC_Spending", header=True, mode="overwrite")
        return DevelopingCOE_TaxRevenue_VS_HC_Spending
    except Exception as e:
        logger.error("No file found")

DevelopingCOE_TaxRevenue_VS_HC_Spending()


