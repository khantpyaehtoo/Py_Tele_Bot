from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to MongoDB server
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB server
client = MongoClient(mongo_uri)

# select database
db = client["mydatabase"]

def dbconnect():
    return db