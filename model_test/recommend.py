import pickle
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer


# Pickled model filepath
MODEL_FILEPATH = "/Users/ekselan/Desktop/Med_Cab_BW/DS-2/data/medcab_model2.pkl"

# Filepath for .csv dataset
DATA_FILEPATH = "/Users/ekselan/Desktop/Med_Cab_BW/DS-2/data/BW_MedCab_Dataset_With_Index.csv"

df = pd.read_csv(DATA_FILEPATH)
df = df.drop('Unnamed: 0', axis=1)
# print(df.shape)
# print(df.head())


def load_model():
    """Function to load pickled nearest neighbors model"""
    # print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model


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

    # Get user provided string
    x = input()  # > this will take-in input from a route

    # Query for symptoms
    new = tfidf.transform([x])

    # Run model
    result = nn.kneighbors(new.todense())

    # Get index location of recommended strain
    num = result[1][0][0]

    # Include all details of strain except Flavor, tokens, data
    info = df.iloc[num][:7]  # > could swap this to database query

    # Possibly grab top 5, loop them and grab their info
    return "Your Recommended Strain:", info


if __name__ == "__main__":

    recommender = load_model()

    print(hello_pickle(recommender))
