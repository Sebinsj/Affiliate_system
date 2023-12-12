from pymongo import MongoClient

client=MongoClient("mongodb+srv://admin:test12@cluster0.ltwxgqs.mongodb.net/?retryWrites=true&w=majority")
db = client.affiliate_db
collection_name = db["affiliate_collection"]



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)