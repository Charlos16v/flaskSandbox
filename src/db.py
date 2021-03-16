from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://charlos:Test22@sandbox.g5xz4.mongodb.net/Sandbox?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Sandbox')
user_collection = pymongo.collection.Collection(db, 'Flask')
