from database import db
from fastapi import APIRouter, HTTPException
from models import StockMarketNews
from schemas import News, NewsResponse

news_router = APIRouter()


# get all news
@news_router.get("/news", response_model=list[NewsResponse])
async def get_all_news(skip: int = 0, limit: int = 10):
    news = db.query(StockMarketNews).offset(skip).limit(limit).all()
    return news


# get a specific news by id
@news_router.get("/news/{news_id}", response_model=NewsResponse)
def get_id_news(news_id: int):
    news = db.query(StockMarketNews).filter(StockMarketNews.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news
