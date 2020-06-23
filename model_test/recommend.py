import pickle
import pandas as pd

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

if __name__ == "__main__":

    recommender = load_model()