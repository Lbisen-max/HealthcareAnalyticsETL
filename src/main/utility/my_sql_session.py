import mysql.connector

def get_mysql_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="HealthCareDataAnalysis"
    )
    return connection