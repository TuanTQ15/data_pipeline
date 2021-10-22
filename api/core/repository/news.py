from ..model.mongodb import db

col = db['rss_news']

def list_news():
    news=list(col.find())
    return news
