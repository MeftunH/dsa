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

def select(table_name, columns, condition=None):
    if condition:
        query = f'SELECT {columns} FROM {table_name} WHERE {condition}'
    else:
        query = f'SELECT {columns} FROM {table_name}'
    return fetchall(query)

def update(table_name, set, condition):
    query = f'UPDATE {table_name} SET {set} WHERE {condition}'
    execute(query)

def delete(table_name, condition):
    query = f'DELETE FROM {table_name} WHERE {condition}'
    execute(query)


def main():
    create_table('users', 'id INTEGER PRIMARY KEY, name TEXT, email TEXT')
    insert('users', 'name, email', 'John Doe')
    select('users', '*', 'name="John Doe"')


if __name__ == '__main__':
    main()