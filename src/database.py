from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

import pandas as pd

SQLALCHEMY_DATABASE_URL = 'sqlite:///my.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

path = os.getcwd()
data = pd.read_csv(f"{path}/data/data.csv", encoding='ISO-8859-1')
df = pd.DataFrame(data)
df.to_sql('data_table', con=engine, if_exists='append')