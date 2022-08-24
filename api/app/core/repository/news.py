from ..model.mongodb import db
import pymongo
col = db['rss_news']

def list_news_latest(category,sources):
    news=list(col.find({"category":category,"source" : {"$in" :sources}}).sort([("published", pymongo.DESCENDING)]).limit(100))
    return news

