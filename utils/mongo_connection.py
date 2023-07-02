
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://sreejithmp007:Muzhutheril007#@cluster0.x9rrkbe.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d={"name":"sravan",
    "email":"sravan@123"}

db=client['mongotest']
coll=db['test']
coll.insert_one(d)