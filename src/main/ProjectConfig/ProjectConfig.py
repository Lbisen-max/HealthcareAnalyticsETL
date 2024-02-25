import os
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, DateType


#AWS Access And Secret key
aws_access_key = "AKIA6OL5CSGFSUO3C6C6"
aws_secret_key = "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"
bucket_name = "heath-analytics-data-bucket"

#local_dataIngestion_dir

anualhealthexpenditure_Global= "C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\annual healthcare expenditure.csv"
childMortVsHealthExpediture_Global="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\child-mortality-vs-health-expenditure.csv"
expenditureOn_NHS_UK="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\expenditure-of-the-national-health-service-nhs-in-the-uk.csv"
healthcareExpendVsGDP_Global="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\healthcare-expenditure-vs-gdp.csv"
healthInsuranceCoverOn_US="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\health-insurance-coverage-in-the-us.csv"
healthProtectionCover_Global="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\health-protection-coverage.csv"
actualExpend_Vs_actualRequirement_Global="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\how-much-we-think-we-spend-on-healthcare-vs-how-much-we-actually-do.csv"
childLifeExpectancy_VS_health_Expend_Global="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\life-expectancy-vs-healthcare-expenditure.csv"
percentageWithoutHeathCover_US="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\percentage-of-persons-without-health-insurance-coverage-us.csv"
domesticSpendingPercentage_HC_GDP="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\public-healthcare-spending-share-gdp.csv"
publicSpendingPercentage_HC_GDP="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\public-health-expenditure-share-GDP-OWID.csv"
publicHealthInsuranceCoverage="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\public-health-insurance-coverage.csv"
outOfPocketExpendOnHealth="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\share-of-out-of-pocket-expenditure-on-healthcare.csv"
outOfPocketExpendOnHealth_VS_GDP="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\share-of-out-of-pocket-expenditure-vs-gdp-per-capita.csv"
TotalShareOfPublicExpenditure_HC_Global="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\share-of-public-expenditure-on-healthcare-by-country.csv"
DevelopingCOE_TaxRevenue_VS_HC_Spending="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\tax-revenue-per-capita-and-public-health-spending-per-capita-in-developing-countries-in.csv"
TotalExpendOn_HC_from_GDP="C:\\Users\\Lokesh Bisen\\Downloads\\archive (2) (1)\\total-healthcare-expenditure-gdp.csv"

# File Download location
local_directory = "D:\\HealthcareAnalyticsETL\\transformData\\"
actualExpend_Vs_actualRequirement_Global_Local="D:\\HealthcareAnalyticsETL\\transformData\\actualExpend_Vs_actualRequirement_Global\\"
destination_path="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\"

# s3_local dirs
actualExpend_Vs_actualRequirement_Global_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-d7bc7d6f-c822-44b5-a6a4-c8ec7606cde7-c000.csv"
anualhealthexpenditure_Global_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-95c1434e-6df1-47a4-b7df-cb936b9f3d8a-c000.csv"
childLifeExpectancy_VS_health_Expend_Global_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-fa0529f2-6e74-42be-b829-2333c87aa648-c000.csv"
childMortVsHealthExpediture_Global_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-ae552cb8-4084-4301-b0f7-e1c764bae116-c000.csv"
DevelopingCOE_TaxRevenue_VS_HC_Spending_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-fa4ee783-4fad-49ca-a3e8-34a8866f0993-c000.csv"
domesticSpendingPercentage_HC_GDP_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-c32393ab-cc55-48e7-8886-23523c4ae852-c000.csv"
expenditureOn_NHS_UK_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-eb04b9f6-7cf3-4b06-972c-1b25b0873570-c000.csv"
healthcareExpendVsGDP_Global_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-44a105ac-780c-4527-938b-259c17788fec-c000.csv"
healthInsuranceCoverOn_US_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-d3708fcf-493c-484e-8b63-53bc5c08c887-c000.csv"
healthProtectionCover_Global_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-6a589800-faee-49d5-b85a-1bc7e6c0554e-c000.csv"
outOfPocketExpendOnHealth_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-dfb34356-b1f9-452c-af8f-b9180fe25758-c000.csv"
outOfPocketExpendOnHealth_VS_GDP_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-1ca36fdd-5891-4e56-aee7-32ff5c8ca4d9-c000.csv"
percentageWithoutHeathCover_US_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-d9b65cf9-1ab5-470e-b496-b7dd56a50da5-c000.csv"
publicHealthInsuranceCoverage_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-04e30344-04e8-480b-9fc0-eb1539bf4ac0-c000.csv"
publicSpendingPercentage_HC_GDP_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-9bcec240-9a13-4e4f-ac4d-392a4a923396-c000.csv"
TotalExpendOn_HC_from_GDP_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-b72c7cdc-a056-4203-96a7-a9a6aebf6dc1-c000.csv"
TotalShareOfPublicExpenditure_HC_Global_s3="D:\\Big_data\HealthcareAnalyticsETL\\ProjectDataFolder\\part-00000-8d546055-a814-4e33-b454-0263fec0fb68-c000.csv"