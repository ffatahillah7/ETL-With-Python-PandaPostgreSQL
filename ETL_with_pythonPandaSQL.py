
# Import Library 

import pandas as pd
from pandasql import sqldf
from sqlalchemy import create_engine

# Database Configuration
db_uri = 'postgresql+psycopg2://postgres:A321654z@localhost:5432/mydb'
#f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Create SQLAlchemy Engine for db connection
engine = create_engine(db_uri)

#Read Csv Dataset from your directory
df_covid_all = pd.read_csv('C:\\Users\\ffatahillah\Documents\\Data Engineer\\de_basic_class_etl-main\\dataset\owid-covid-data.csv')
print(df_covid_all)

# Using panda SQL , Query with where clause 
df_idn = sqldf(''' select * from df_covid_all where total_cases is not null and total_deaths is not null and location ='Indonesia' and 
new_deaths > 5 ''')

#print(df_idn)
#df_idn.describe()

# Count all the records
count_data = df_idn.shape[0]

#load data after transformation to postgresql
TABLE_NAME = 'test'
df_idn.to_sql(name=TABLE_NAME, con=engine,index=False,if_exists='append')
print(f'Total Record has been inserted are {count_data} to table {TABLE_NAME} ')