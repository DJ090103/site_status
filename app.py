from fastapi import FastAPI
from pydantic import BaseModel
import requests
import datetime 

app = FastAPI()

class Siteinfo(BaseModel) :
    siteurl : str

@app.post("/siteinfo")
def siteinfo(site : Siteinfo) :
    response = requests.get(site)
    status_code = response.status_code
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "message" : {
            "url" : site,
            "status" : status_code,
            "curr_timestamp " : current_time
        }
    }

@app.get("/hello")
def say_hello():
    return { "message": "Hello, Dhiraj!" }
# Define the expected request body
class UserInfo(BaseModel):
    name: str
    age: int

@app.post("/greet")
def greet_user(user: UserInfo):
    return {
        "message": f"Hello {user.name}, you are {user.age} years old!"
    }

class Details(BaseModel):
    name : str
    age : int
    location : str
@app.post("/details")

def user_detaiils(user:Details):
    if user.location == "Mumbai" :
        return {
            "message": f"Hello {user.name} ({user.age}) is from  My favourite City ({user.location})"
        }
    else :
        return{
            "message": f"Hello {user.name} ({user.age}) is from ({user.location})"
        }

