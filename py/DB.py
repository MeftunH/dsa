import sqlite3
import MySQLdb

interface = 'sqlite'
db = 'db.sqlite3'

def connect():
    if interface == 'sqlite':
        return sqlite3.connect(db)
    elif interface == 'mysql':
        return MySQLdb.connect(host='localhost', user='username', passwd='password', db='database_name')

def get_cursor():
    return connect().cursor()

def execute(query, args=None):
    if args:
        get_cursor().execute(query, args)
    else:
        get_cursor().execute(query)
    connect().commit()

def fetchone(query, args=None):
    if args:
        get_cursor().execute(query, args)
    else:
        get_cursor().execute(query)
    return get_cursor().fetchone()

def fetchall(query, args=None):
    if args:
        get_cursor().execute(query, args)
    else:
        get_cursor().execute(query)
    return get_cursor().fetchall()

def close():
    get_cursor().close()
    connect().close()

def create_table(table_name, columns):
    query = f'CREATE TABLE {table_name} ({columns})'
    execute(query)

def drop_table(table_name):
    query = f'DROP TABLE {table_name}'
    execute(query)

def insert(table_name, columns, values):
    query = f'INSERT INTO {table_name} ({columns}) VALUES ({values})'
    execute(query)
