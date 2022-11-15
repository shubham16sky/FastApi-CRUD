from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional
from pymongo import MongoClient



app = FastAPI()
#mongo configuration
#connecting to defualt host and port
client = MongoClient('mongodb://db:27017/')
#creating a database named users
db = client['userDB']
#creating collection
collection = db['user_coll']

#now defining the class users 

class User(BaseModel):
    name : str
    account_no : int=Field(alias="_id")
    email : str
    birthdate : str
    
    
#route to search user by id 

@app.get("/get_users")

def get_all_users():
    db = client['userDB']
    collection = db['user_coll']
    data = collection.find()
    users=[]
    
    for items in data:
        
        users.append(User(**items))
        
    return {"users":users}
    
    
    
    
#route to add users
@app.post("/add_user")
def add_user(user_data:User):
    db = client['userDB']
#creating collection
    collection = db['user_coll']

    data=collection.insert_one(user_data.dict())
    if data.acknowledged:
        return {"message":"User added"}
    return {"message":"Error in adding user"}



@app.get("/get_users_by_acc/{accNO}")

def get_all_users(accNO:int):
    db = client['userDB']
    collection = db['user_coll']
    data = collection.find({"account_no":accNO})
    users=[]
    
    for items in data:
        
        users.append(User(**items))
        
    return {"user":users}
    


    


    
        
    

