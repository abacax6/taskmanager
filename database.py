from pymongo import MongoClient

client = MongoClient(
    "mongodb://admin:admin123@localhost:27017/"
)

db = client["taskmanager"]

tasks_collection = db["tasks"]