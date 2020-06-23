# our routes for json

from flask import Blueprint


import os
from dotenv import load_dotenv
import psycopg2
import pandas
import csv

# ENV_PATH = os.path.join(os.getcwd(), '.env')
# > loads contents of the .env file into the script's environment
# load_dotenv(ENV_PATH)
load_dotenv()

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


'''
Create Table called medcab !
'''
create = '''
CREATE TABLE medcab(strain VARCHAR,id INT,flavors VARCHAR,effects VARCHAR,
medical VARCHAR,type VARCHAR,rating FLOAT,flavor VARCHAR);
'''
# query = create
# cursor.execute(query)

connection.commit()

'''
Fill in table:
'''
with open('BW_MedCab_Dataset.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO medcab VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", row
        )

connection.commit()

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
