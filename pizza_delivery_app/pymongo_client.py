import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

dbname = client['pizza_db']

id_collection = dbname.get_collection("id_collection")
pizza_collection = dbname.get_collection("pizza_collection")

