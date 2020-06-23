# our routes for json

from flask import Blueprint


import os
from dotenv import load_dotenv
import psycopg2
import pandas

ENV_PATH = os.path.join(os.getcwd(), '.env')
# > loads contents of the .env file into the script's environment
load_dotenv(ENV_PATH)


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

# cursor.execute('SELECT * from test_table;')
# result = cursor.fetchall()
# print("RESULT:", type(result))
# print(result)

# app = Flask(__name__)

# Instantiate new blueprint object
home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    return "Hello, we're here to help."


@home_routes.route("/strains")
def strains():
    return "This will list the strains"


@home_routes.route("/recx")
def recommendations():
    return "This will list recommendations"
