from fastapi import FastAPI
from core.routers import news,user
app = FastAPI()

app.include_router(news.router)
app.include_router(user.router)