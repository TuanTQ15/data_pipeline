from fastapi import FastAPI
from pymongo import MongoClient
app = FastAPI()
MONGODB_URL="mongodb://rss_news:rss_news@localhost:27017/"

client =MongoClient(MONGODB_URL)
db = client['rss_news']














