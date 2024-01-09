import psycopg2
import geopandas

def create_connection(database):
    connection = None
    # try:
    connection = psycopg2.connect(
        database=database,
        user='postgres',
        password='postsuperzax',
        host='localhost',
        port=5432,
    )
    print("Connection to PostgreSQL DB successful")
    # except OperationalError as e:
    #     print(f"The error '{e}' occurred")
    return connection

def select_query(sql, connection):
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()
    # connection.commit()
    # cursor.close()