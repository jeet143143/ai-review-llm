from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")  

client = MongoClient(MONGO_URI)
db = client["review_db"]
collection = db["customer_reviews"]

def get_reviews():
    return [doc["review"] for doc in collection.find({}, {"_id": 0, "review": 1})]