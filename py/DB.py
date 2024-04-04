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
