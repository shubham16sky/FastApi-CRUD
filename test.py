from pymongo import MongoClient
import pprint 



client= MongoClient()

DB = client['userDB']

coll = DB['user_coll']

data = coll.find()
for item in data:
    print(item)



