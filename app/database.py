import os 
from pymongo import MongoClient
from dotenv import load_dotenv


# Connecting to mongoDB 
load_dotenv()
URI = os.environ.get("URI")
client = MongoClient(URI) 


# Creating database and collections 
db = client["school"]
students_collection = db["students"]
subjects_collection = db["subjects"]
teachers_collection = db["teachers"]
academic_records_collection = db["academic"]