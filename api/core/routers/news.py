from typing import  List
from fastapi import APIRouter
from ..repository import news
from ..model import  models as md
router = APIRouter(prefix="/api/news", tags=['News'])
@router.get('/',response_description="List all News", response_model=List[md.NewsModel])
def list_news():
    return news.list_news()