import os
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, DateType

anualhealthexpenditure_Global_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Indicator:Current health expenditure (CHE) per capita in PPP int$",StringType(),True)
])

childMortVsHealthExpediture_Global_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Mortality rate, under-5 (per 1,000 live births)",FloatType(),True),
    StructField("Current health expenditure per capita, PPP (current international $)",FloatType(),True),
    StructField("Population (historical estimates)",FloatType(),True),
    StructField("Continent",StringType(),True)
])

expenditureOn_NHS_UK_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("NHS Expenditure %GDP 1950-2012 (Office of Health Economics (2012))",FloatType(),True)
])

healthcareExpendVsGDP_Global_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Current health expenditure per capita, PPP (current international $)",FloatType(),True),
    StructField("GDP per capita, PPP (current international $)",FloatType(),True),
    StructField("Population (historical estimates)",FloatType(),True),
    StructField("Continent",StringType(),True)
])

healthInsuranceCoverOn_US_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Health Insurance Coverage US, Govt Plan (US Current Population Survey (2014))",FloatType(),True),
    StructField("Health Insurance Coverage US, Private Plan (US Current Population Survey (2014))",FloatType(),True),
    StructField("Health Insurance Coverage US, Any Plan (US Current Population Survey (2014))",FloatType(),True)
])

healthProtectionCover_Global_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Share of population covered by health insurance (ILO (2014))",FloatType(),True)
])

actualExpend_Vs_actualRequirement_Global_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("How much we actually spend on health expenditure (IPSOS (2016))",FloatType(),True),
    StructField("How much we think we spend on health expenditure (IPSOS (2016))", FloatType(), True),
    StructField("Population (historical estimates)", FloatType(), True),
    StructField("Continent", StringType(), True)
])


childLifeExpectancy_VS_health_Expend_Global_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Life expectancy at birth, total (years)",FloatType(),True),
    StructField("Current health expenditure per capita, PPP (current international $)", FloatType(), True),
    StructField("Population (historical estimates)", FloatType(), True),
    StructField("Continent", StringType(), True)
])

percentageWithoutHeathCover_US_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Percentage of persons without health insurance (%)",FloatType(),True)
])


domesticSpendingPercentage_HC_GDP_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Domestic general government health expenditure (% of GDP)",FloatType(),True)
])

publicSpendingPercentage_HC_GDP_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("public_health_expenditure_pc_gdp",FloatType(),True)
])


publicHealthInsuranceCoverage_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Health Insurance Coverage (Tanzi & Schuknecht (2000))",IntegerType(),True)
])

outOfPocketExpendOnHealth_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Out-of-pocket expenditure (% of current health expenditure)",FloatType(),True)
])

outOfPocketExpendOnHealth_VS_GDP_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Out-of-pocket expenditure (% of current health expenditure)",FloatType(),True),
    StructField("GDP per capita, PPP (constant 2017 international $)",FloatType(),True),
    StructField("Population (historical estimates)",FloatType(),True),
    StructField("Continent",StringType(),True),
    ])

TotalShareOfPublicExpenditure_HC_Global_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Domestic general government health expenditure (% of current health expenditure)",FloatType(),True)
])

DevelopingCOE_TaxRevenue_VS_HC_Spending_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Tax revenues per capita in developing countries (PPP) (World Bank (WDI) (2017))",FloatType(),True),
    StructField("Public expenditure on health per capita in developing countries (PPP) (World Bank (WDI) (2017))",FloatType(),True),
    StructField("Continent",StringType(),True),
    StructField("Population (historical estimates)",FloatType(),True)
])

TotalExpendOn_HC_from_GDP_schema = StructType([
    StructField("Entity",StringType(),True),
    StructField("Code",StringType(),True),
    StructField("Year",IntegerType(),True),
    StructField("Indicator:Current health expenditure (CHE) as percentage of gross domestic product (GDP) (%)",FloatType(),True)
])