from typing import  List
from fastapi import APIRouter,Query
from ..repository import news
from ..model import  models as md
router = APIRouter(prefix="/api/news", tags=['News'])
@router.get('/latest',response_description="List all News")
def list_news(category: str,sources: list = Query([])):
    return news.list_news_latest(category,sources)