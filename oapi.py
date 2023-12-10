# RUN WITH COMMAND python oapi.py
# I could use a CRON job to automate data retrieval?
import requests

# Overpass query
query = """
[out:json];
(
  node["amenity"="cafe"](37.7793,-122.4192,37.7893,-122.4092);
  way["amenity"="cafe"](37.7793,-122.4192,37.7893,-122.4092);
  relation["amenity"="cafe"](37.7793,-122.4192,37.7893,-122.4092);
);
out body;
>;
out skel qt;
"""

# Overpass API URL
url = "http://overpass-api.de/api/interpreter"

# Send the request
response = requests.get(url, params={'data': query})
data = response.json()

# Print the result
# print(data)
# print(data['elements'][0])
print(data['elements'][0]['lat'])
print(data['elements'][0]['lon'])
print(data['elements'][0]['tags']['name'])
print(data['elements'][1]['lat'])
print(data['elements'][1]['lon'])
print(data['elements'][1]['tags']['name'])
x = input('press to continue')

import psycopg2

def create_connection():
    connection = None
    # try:
    connection = psycopg2.connect(
        database='locationtestdb',
        user='postgres',
        password='postsuperzax',
        host='localhost',
        port=5432,
    )
    print("Connection to PostgreSQL DB successful")
    # except OperationalError as e:
    #     print(f"The error '{e}' occurred")
    return connection

connection = create_connection()
x = input('press to continue')

def insert_location(connection, coffee_shop, lat, long):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO locations (coffee_shop, lat, lon) 
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (coffee_shop, lat, long))
    connection.commit()
    cursor.close()

# Example: Inserting a new location
insert_location(connection, data['elements'][0]['tags']['name'], data['elements'][0]['lat'], data['elements'][0]['lon'])
insert_location(connection, data['elements'][1]['tags']['name'], data['elements'][1]['lat'], data['elements'][1]['lon'])
x = input('press to continue')

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
    'dbname': 'locationtestdb'
}
# sql_str = 'postgresql://{user}:{password}@{host}:{port}/{dbname}'.format
# db_connection = create_engine(sql_str(**db_info))
db = SQLDatabase.from_uri("postgresql://postgres:postsuperzax@localhost:5432/locationtestdb")
llm = OpenAI(openai_api_key = "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", temperature=0, verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# db_chain.run("How many neighborhoods are there in nyc?")
# db_chain.run("What streets are within 10 meters of the Broad Street subway station?")
# db_chain.run("What neighborhood is the 'Broad St' station in?")
# db_chain.run("Using spatial joins, can you tell me what neighborhood the 'Broad St' station is in?")
# db_chain.run("Using ST_Contains and spatial joins, can you tell me what neighborhood the 'Broad St' station is in?")
db_chain.run("Which coffee shop is nearest to Angel Cafe & Deli?")
x = input('press to continue')