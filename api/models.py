from database import Base
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String


class StockMarketNews(Base):
    __tablename__ = "stockmarket_news_stockmarketnews"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(String, index=True)
    banner_image = Column(String, index=True)
    authors = Column(String, index=True)
    time_published = Column(DateTime, index=True)
    source = Column(String, index=True)
    overall_sentiment_label = Column(String, index=True)
    overall_sentiment_score = Column(Float, index=True)
    url = Column(String, index=True)


class StockMarketData(Base):
    __tablename__ = "stockmarket_data_stockmarketdata"

    id = Column(Integer, primary_key=True, index=True)
    stock_symbol = Column(String, index=True)
    from_date = Column(DateTime, index=True)
    after_hours = Column(Float, index=True)
    at_close = Column(Float, index=True)
    high = Column(Float, index=True)
    low = Column(Float, index=True)
    at_open = Column(Float, index=True)
    pre_market = Column(Float, index=True)
    status = Column(String, index=True)
    volume = Column(Float, index=True)
    otc = Column(Boolean, index=True)
    sma = Column(Float, index=True)
    ema = Column(Float, index=True)
    macd = Column(Float, index=True)
    rsi = Column(Float, index=True)
