import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class Conn:
  def __init__(self,username,password,host,port,database):
    self.engine = create_engine('postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'.format(
    username=username,password=password,host=host,port=port,database=database))
  
  def execSQL(self,sql):
    data = pd.read_sql(sql,con=self.engine.connect())
    return data