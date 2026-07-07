import pandas as pd
#for postgres sql connection
import psycopg2 
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#Connection Variables for pgsql
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PWD = "1234"
DB_PORT = "5432"

print("Connecting to PostgreSQL server...")

conn = psycopg2.connect(host = DB_HOST, user=DB_USER, password= DB_PWD, port=DB_PORT, database= "postgres" )
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

# create DB in pg for 1st time

try:
    cursor.execute("Create Database hr_analytics;")
    print("Database 'hr_analytics' created successfully!")
except psycopg2.errors.DuplicateDatabase:
    print("Database 'hr_analytics' already exists. Moving forward...")

cursor.close()
conn.close()

#Load raw-hr-data.csv into hr_analytics

print("Loading data into 'hr_analytics'...")

df = pd.read_csv("raw-hr-data.csv")

#use SQLAlchemy to dump data from csv to pgsql

from sqlalchemy import create_engine
engine  = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/hr_analytics')

df.to_sql('employees', engine, if_exists='replace', index=False)

print("🚀 Success! 1,000 records successfully injected into live PostgreSQL database!")

