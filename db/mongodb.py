from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['social_media_management']