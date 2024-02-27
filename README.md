# Heath Care Expenditure Analysis | End-To-End Data Engineering Project

The objective is to build a pipeline for ingesting, storing, processing, and visualizing healthcare data to derive actionable insights for improving healthcare outcomes and informing policy decisions.

# Tech Stack
* Data lake: Amazon S3
* Data source: Local
* Processing layer: Apache Spark
* Visualization: AWS QuickSight
* Python
  

  # Phases
  ## 1.  Data Acquisition
  Acquire the data listed in the project resources. This initial collection included data loading into local system.
  List the dataset(s) acquired :
  * anualhealthexpenditure_Global
  * childLifeExpectancy_VS_health_Expend_Global
  * childMortVsHealthExpediture_Global
  * DevelopingCOE_TaxRevenue_VS_HC_Spending
  * domesticSpendingPercentage_HC_GDP
  * expenditureOn_NHS_UK
  * healthcareExpendVsGDP_Global
  * healthInsuranceCoverOn_US
  * healthProtectionCover_Global
  * outOfPocketExpendOnHealth
  * outOfPocketExpendOnHealth_VS_GDP
  * percentageWithoutHeathCover_US
  * publicHealthInsuranceCoverage
  * publicSpendingPercentage_HC_GDP
  * TotalExpendOn_HC_from_GDP
  * TotalShareOfPublicExpenditure_HC_Global
 
  ## 2. Data Understanding
  1. Structure Investigation : Checked general shape of the datasets, as well as the data types of features.
     
  2. Quality Investigation : The main goal to have a global view on the datasets with regards to things like duplicate values,missing values and unwanted entries or recording errors.
      here I found there are many missing values. additionaly, some of the column like "Population" are duplicated. "Country code", "Continents" columns has huge missing data hecne decided
     to drop those coluimns. furthermore I observed that table like "childLifeExpectancy_VS_health_Expend_Global" has valid and authentic data from year 1960 hence decided to remove all unwanted
     data.

# Folder Structure 

├───.idea
│   └───inspectionProfiles
├───src
│   ├───main
│   │   ├───ProjectConfig
│   │   │   └───__pycache__
|   |   |   └───ProjectConfig.py
|   |   |   └───ProjectSchema.py
|   |   |   └───requirement.txt
│   │   ├───PythonSparkJobs
│   │   │   ├───spark-warehouse
|   |   |   ├───CleanAndTransformed.py
|   |   |   ├───DataIngestion.py
│   │   │   └───__pycache__
│   │   ├───utility
│   │   │   └───__pycache__
|   |   |   ├───logging_config.py
|   |   |   ├───my_sql_session.py
|   |   |   ├───s3_client_object.py
|   |   |   ├───spark_session.py
|   |   |   ├───test.py
│   │   └───__pycache__
│   └───__pycache__
└───transformData
    ├───actualExpend_Vs_actualRequirement_Global
    ├───anualhealthexpenditure_Global
    ├───childLifeExpectancy_VS_health_Expend_Global
    ├───childMortVsHealthExpediture_Global
    ├───DevelopingCOE_TaxRevenue_VS_HC_Spending
    ├───domesticSpendingPercentage_HC_GDP
    ├───expenditureOn_NHS_UK
    ├───healthcareExpendVsGDP_Global
    ├───healthInsuranceCoverOn_US
    ├───healthProtectionCover_Global
    ├───outOfPocketExpendOnHealth
    ├───outOfPocketExpendOnHealth_VS_GDP
    ├───percentageWithoutHeathCover_US
    ├───publicHealthInsuranceCoverage
    ├───publicSpendingPercentage_HC_GDP
    ├───TotalExpendOn_HC_from_GDP
    └───TotalShareOfPublicExpenditure_HC_Global


# Data Ingestion and Data Transformation using Pyspark (ETL)

Downloaded the necessary libraries. imported spark and performed required transformed functions also. Created a config file under projectconfig folder which contains required ingestion path and schema of the tables. After transformation data rewritten into local and aws S3 server for further analysis. additionaly , AWS S3 connected with the AWS quicksight for visual data understanding.

![image](https://github.com/Lbisen-max/HealthcareAnalyticsETL/assets/79071673/48e08f40-660c-4972-8120-f0a01bb3e67c)

![image](https://github.com/Lbisen-max/HealthcareAnalyticsETL/assets/79071673/d9dae1a6-981a-496d-8dad-583aa3bca60f)

![image](https://github.com/Lbisen-max/HealthcareAnalyticsETL/assets/79071673/d7a8df95-5a08-49d2-8acf-45fbc23fda7d)

![image](https://github.com/Lbisen-max/HealthcareAnalyticsETL/assets/79071673/3acbeef5-bd92-4857-a329-507cc4cb4a92)

![image](https://github.com/Lbisen-max/HealthcareAnalyticsETL/assets/79071673/6cee7a16-e55f-4a38-973c-a1c9bf7fe3e6)

![image](https://github.com/Lbisen-max/HealthcareAnalyticsETL/assets/79071673/0db95946-3145-43cf-8924-81aa1c48612e)

![image](https://github.com/Lbisen-max/HealthcareAnalyticsETL/assets/79071673/b4ac303e-e895-4a33-a64a-5bea8670c2e0)













     
  
  

