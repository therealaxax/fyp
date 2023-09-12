# import sys
# print(sys.path)

# sys.path.append('C:\\Users\\Gareth Thong\\anaconda3\\envs\\geoenv')

from sqlalchemy import create_engine
import geopandas
db_info = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'postsuperzax',
    'port': 5432,
    'dbname': 'nyc'
}
sql_str = 'postgresql://{user}:{password}@{host}:{port}/{dbname}'.format
db_connection = create_engine(sql_str(**db_info))

sql = "SELECT * FROM nyc_neighborhoods"
df = geopandas.GeoDataFrame.from_postgis(sql, db_connection) 
print(df)
# df = geopandas.GeoDataFrame.read_postgis(sql, db_connection) 
# c = db_connection.execute("SELECT * FROM nyc_neighborhoods")
# c.next()

# x=input("here")