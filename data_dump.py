import pymongo
import pandas as pd
import json


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://NagendraSethi:p23cs026@cluster0.navdqbm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

DATA_FILE_PATH=(r"D:\project\ML project\insurance-premium-prediction\insurance.csv")
DATABASE_NAME="INSURANCE"
COLLECTION_NAME="INSURANCE_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values()) #df ko transepose kiya json fomat me
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)   