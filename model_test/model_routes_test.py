import pickle
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Blueprint
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

# Instantiate new blueprint object
model_routes = Blueprint("model_routes", __name__)


# Pickled model filepath
# MODEL_FILEPATH = "/Users/ekselan/Desktop/Med_Cab_BW/DS-2/data/medcab_model2.pkl"
MODEL_PATH = os.path.join(os.path.dirname(__file__), "medcab_model2_copy.pkl")


# ### Filepath for .csv dataset
# DATA_URL = "https://raw.githubusercontent.com/BW-Med-Cab-2/DS/master/data/BW_MedCab_Dataset_With_Index.csv"

# breakpoint()
# ### Create df for model to reference for strain info
# df = pd.read_csv("https://raw.githubusercontent.com/BW-Med-Cab-2/DS/master/data/BW_MedCab_Dataset_With_Index.csv")
# df = df.drop('Unnamed: 0', axis=1)
# # print(df.shape)
# # print(df.head())

"""Establish db connection instead of using csv"""

# Creating connection object inside function to sustain connection
# until session end
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST)
cursor = connection.cursor()

query = """
    SELECT *
    FROM medcab
    """
# Execute query
cursor.execute(query)
# Query results
strains = list(cursor.fetchall())
# Key-value pair names for df columns
columns = ["strain",
           "id",
           "flavors",
           "effects",
           "medical",
           "type",
           "rating",
           "flavor"]
# List of tuples to DF
df = pd.DataFrame(strains, columns=columns)
# print(type(df))

# DF to dictionary
pairs = df.to_json(orient='records')
# print(type(pairs))

# return pairs

# Function to load model


def load_model():
    """Function to load pickled nearest neighbors model"""
    # print("LOADING THE MODEL...")
    with open(MODEL_PATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model

# Function to generate recommendation


def hello_pickle(nn):
    """
    Function to use pickled model to get nearest neighbor recommendation
    nn = pickled model
    """
    nn = nn

    # List of text documents
    data = list(df['medical'])

    # create the transformer
    tfidf = TfidfVectorizer(max_df=.95,
                            min_df=2,
                            ngram_range=(1, 3),
                            max_features=5000)

    # build vocab
    dtm = tfidf.fit_transform(data)  # > Similar to fit_predict

    # Get user provided string, currently have placeholder string for example
    x = "Loss of appetite, anxiety"  # > this will take-in input from a route

    # Query for symptoms
    new = tfidf.transform([x])

    # Run model
    result = nn.kneighbors(new.todense())

    # For loop to grab top 5 recommendations
    summary = []
    for r in result[1][0]:
        info = df.iloc[r][:7]
        summary.append(info)

    # Possibly grab top 5, loop them and grab their info
    return summary


@model_routes.route("/model")
def run_model():

    recommender = load_model()
    result = hello_pickle(recommender)
    # Turn Series into json
    res = result[0].to_json()
    return res


""" Add dynamic route for model_routes"""

"""Tweak hello_pickle function for use with input variable"""
def hello_recommender(nn, x):
    """
    Function to use pickled model to get nearest neighbor recommendation
    nn = pickled model
    x = input string
    """
    nn = nn
    x = x

    # List of text documents
    data = list(df['medical'])

    # create the transformer
    tfidf = TfidfVectorizer(max_df=.95,
                            min_df=2,
                            ngram_range=(1, 3),
                            max_features=5000)

    # build vocab
    dtm = tfidf.fit_transform(data)  # > Similar to fit_predict

    # Query for symptoms
    new = tfidf.transform([x])

    # Run model
    result = nn.kneighbors(new.todense())

    # For loop to grab top 5 recommendations
    summary = []
    for r in result[1][0]:
        info = df.iloc[r][:7]
        summary.append(info)

    # Possibly grab top 5, loop them and grab their info
    return summary

@model_routes.route("/model/<symptoms_string>")
def make_rec(symptoms_string=None):
    x = symptoms_string

    recommender = load_model()
    result = hello_recommender(recommender, x)
    res = result[0].to_json()
    return res

# Closing Connection
connection.close()
