# our routes for json

from flask import Flask


import os
from dotenv import load_dotenv
import psycopg2
import pandas

load_dotenv()  # > loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)

connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

# Close connection
connection.close()

# cursor.execute('SELECT * from test_table;')
# result = cursor.fetchall()
# print("RESULT:", type(result))
# print(result)

# app = Flask(__name__) #> Turned off in testing
# in case duplicate app objects were conflicting


# @app.route("/")
# def index():
#     return "Hello, we're here to help."


# @app.route("/strains")
# def strains():
#     return "This will list the strains"


# @app.route("/recx")
# def recommendations():
#     return "This will list recommendations"
