import pymysql
#import yaml
from constants import *

#credentials = yaml.load(open('./credentials.yml'))

#DB_HOST = credentials['database']['hostname']
#DB_USER = credentials['database']['username']
#DB_PASSWORD = credentials['database']['password']
#DB_NAME = 'dli'


def insert_into_bol_table(stop_id, bol_number, weight, pieces, sequence, unique_id):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, autocommit=True)
    cursor = conn.cursor()
    sql = "INSERT INTO bol (stop_id, bol_number, weight, pieces, sequence, unique_id) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (stop_id, bol_number, weight, pieces, sequence, unique_id))
    data = cursor.fetchall()
    print(data)
    conn.close()


def get_all_columns():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM bol'
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)


def drop_table_bol():
    db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = db.cursor()
    sql = 'DROP TABLE bol'
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)


def create_table_bol():
    db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = db.cursor()
    sql = 'CREATE TABLE bol ( stop_id varchar(255), bol_number varchar(255), weight decimal(7), pieces varchar(255), sequence varchar(255), unique_id varchar(255) ) '
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    

def delete_from_bol_table():
    db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = db.cursor()
    sql = "DELETE FROM bol WHERE stop_id = '123'"
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchone()
    print(data)
    db.close()



