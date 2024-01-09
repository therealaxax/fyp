# RUN WITH COMMAND python postgistest.py
# import sys
# print(sys.path)

# sys.path.append('C:\\Users\\Gareth Thong\\anaconda3\\envs\\geoenv')

from sqlalchemy import create_engine
import geopandas
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain

db_info = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'postsuperzax',
    'port': 5432,
    'dbname': 'nyc'
}
# sql_str = 'postgresql://{user}:{password}@{host}:{port}/{dbname}'.format
# db_connection = create_engine(sql_str(**db_info))
db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/nyc")
llm = OpenAI(openai_api_key = "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", temperature=0, verbose=True, model="gpt-3.5-turbo-instruct")
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# db_chain.run("How many neighborhoods are there in nyc?")
# db_chain.run("What streets are within 10 meters of the Broad Street subway station?")
# db_chain.run("What neighborhood is the 'Broad St' station in?")
# db_chain.run("Using spatial joins, can you tell me what neighborhood the 'Broad St' station is in?")
# db_chain.run("Using ST_Contains and spatial joins, can you tell me what neighborhood the 'Broad St' station is in?")
# db_chain.run("By specifying which table the column names are from, and by using ST_Contains and spatial joins, can you tell me what neighborhood the 'Broad St' station is in?")
db_chain.run("Using the nyc_neighborhoods and nyc_subway_stations tables and by specifying which table the column names are from, and by using ST_Contains and spatial joins, can you tell me what neighborhood the 'Broad St' station is in?")
# db_chain.run("What is the average length of residential streets in nyc?")
# db_chain.run("By using the ST_Length function, what is the average length of residential streets in nyc?")
# db_chain.run("By using the ST_Length function, what is the average length of residential streets in nyc? State the result in feet.")
# db_chain.run("By using the ST_Length function, what is the average length of residential streets in nyc? Note that the database returns results in feet.")

def testquery():
    sql = "SELECT * FROM nyc_neighborhoods"
    df = geopandas.GeoDataFrame.from_postgis(sql, db_connection) 
    print(df)

def query():
    print("hello")
    return 0
# df = geopandas.GeoDataFrame.read_postgis(sql, db_connection) 
# c = db_connection.execute("SELECT * FROM nyc_neighborhoods")
# c.next()

# x=input("here")