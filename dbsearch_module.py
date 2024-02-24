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
    results = cursor.fetchall()
    # Convert results to a dictionary with column 1 as keys and column 2 as values
    results_dict = {row[0]: row[1] for row in results}
    cursor.close()
    return results_dict

def select_query_list(sql, connection):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    resultlist = [result[0] for result in results]
    return resultlist

def insert_single_col_fewshots(connection, query, question):
    sql = "INSERT INTO fewshotexamples (query, question) VALUES (%s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql, (question, query))
    connection.commit()
    print("Fewshot insertion success")

def insert_single_col_propernouns(connection, propernoun):
    sql = f"INSERT INTO propernouns (propernoun) VALUES ('{propernoun}')"
    cursor = connection.cursor()
    cursor.execute(sql, propernoun)
    connection.commit()
    print("Proper noun insertion success")