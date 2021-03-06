# our routes for json

from flask import Blueprint
import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd



# ENV_PATH = os.path.join(os.getcwd(), '.env')
# > loads contents of the .env file into the script's environment
# load_dotenv(ENV_PATH)
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)

# connection = psycopg2.connect(
#     dbname=DB_NAME,
#     user=DB_USER,
#     password=DB_PASSWORD,
#     host=DB_HOST)
# print("CONNECTION:", connection)

# cursor = connection.cursor()
# print("CURSOR:", cursor)


# '''
# Create Table called medcab !
# '''
# create = '''
# CREATE TABLE medcab(strain VARCHAR,id INT,flavors VARCHAR,effects VARCHAR,
# medical VARCHAR,type VARCHAR,rating FLOAT,flavor VARCHAR);
# '''


# |^|^|^| Commented out section above to try and reduce num of connections |^|^|^|


# query = create
# cursor.execute(query)

# connection.commit()

# '''
# Fill in table:
# '''
# with open('BW_MedCab_Dataset.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         cursor.execute(
#             "INSERT INTO medcab VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", row
#         )

# connection.commit()


home_routes = Blueprint("home_routes", __name__)


def fetch_strains(query):
    # Creating connection object inside function to sustain connection
    # until session end
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST)
    cursor = connection.cursor()

    # Execute query
    cursor.execute(query)
    # Query results
    strains = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = ["id",
               "strain",
               "rating"]
    # List of tuples to DF
    df = pd.DataFrame(strains, columns=columns)
    print(type(df))

    # DF to dictionary
    pairs = df.to_json(orient='records')
    print(type(pairs))
    # Closing Connection
    connection.close()
    return pairs

def fetch_top(query):
    # Creating connection object inside function to sustain connection
    # until session end
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST)
    cursor = connection.cursor()

    # Execute query
    cursor.execute(query)
    # Query results
    strains = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = ["strain"]
    # List of tuples to DF
    df = pd.DataFrame(strains, columns=columns)
    print(type(df))

    # DF to dictionary
    pairs = df.to_json(orient='records')
    print(type(pairs))
    # Closing Connection
    connection.close()
    return pairs

def fetch_data(query):
      # Creating connection object inside function to sustain connection
    # until session end
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST)
    cursor = connection.cursor()

    # Execute query
    cursor.execute(query)
    # Query results
    strains = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = ["strain", "id",
                "flavors",
                "effects",
                "medical",
                "type",
                "rating",
                "flavor"]
    # List of tuples to DF
    df = pd.DataFrame(strains, columns=columns)
    # DF to dictionary
    pairs = df.to_json(orient='records')
    # Closing Connection
    connection.close()
    return pairs

@home_routes.route("/")
def index():
    return "Hello, we're here to help."


@home_routes.route("/strains")
def strains():
    query = '''
    SELECT id, strain, rating
    FROM medcab
    '''
    return fetch_strains(query)


@home_routes.route("/recx")
def recommendations():
    return "This will list recommendations."

@home_routes.route("/data")
def data():
    query = """
    SELECT *
    FROM medcab
    """
    return fetch_data(query)

@home_routes.route("/toptenrating")
def toprating():
    query = """
    SELECT strain
    FROM medcab
    where rating >= 5.0
    ORDER BY LENGTH(medical) DESC
    LIMIT 10
    """
    return fetch_top(query)


@home_routes.route("/toptenflavor")
def topflavor():
    query = """
    SELECT strain
    FROM medcab
    ORDER BY LENGTH(flavors) DESC
    LIMIT 10
    """
    return fetch_top(query)