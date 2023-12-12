from pymongo import MongoClient

client=MongoClient("mongodb+srv://admin:test1234@cluster0.ltwxgqs.mongodb.net/?retryWrites=true&w=majority")
db=client.as_db
co