'''
Created on 24 janv. 2018

@author: Jonathan
'''
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)"
cursor.execute(create_users)

create_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)"
cursor.execute(create_items)

# cursor.execute("INSERT INTO items VALUES ('table', 1295.99)")

connection.commit();
connection.close()