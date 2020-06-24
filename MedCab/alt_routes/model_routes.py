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

### Instantiate new blueprint object
model_routes = Blueprint("model_routes", __name__)


### Pickled model filepath
MODEL_FILEPATH = "/Users/ekselan/Desktop/Med_Cab_BW/DS-2/data/medcab_model2.pkl"

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
columns = ["id",
            "strain",
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

### Function to load model


def load_model():
    """Function to load pickled nearest neighbors model"""
    # print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model

### Function to generate recommendation
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
                        ngram_range=(1,3),
                        max_features=5000)

    # build vocab
    dtm = tfidf.fit_transform(data) #> Similar to fit_predict

    # Get user provided string, currently have placeholder string for example
    x = "Aches, pain, insomnia, fatigue" #> this will take-in input from a route 

    # Query for symptoms
    new = tfidf.transform([x])  

    # Run model
    result = nn.kneighbors(new.todense())   

    # Get index location of recommended strain
    num = result[1][0][0]   

    # Include all details of strain except Flavor, tokens, data
    info = df.iloc[num][:7] #> could swap this to database query 

    # Possibly grab top 5, loop them and grab their info    
    return "Your Recommended Strain:", info

@model_routes.route("/model")
def run_model():

    recommender = load_model()

    return "hello_pickle(recommender)"

# Closing Connection
connection.close()