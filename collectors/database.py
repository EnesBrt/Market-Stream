from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Use environment variables for database configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "market_admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123456")
DB_NAME = os.getenv("DB_NAME", "market_stream")
DB_PORT = os.getenv("DB_PORT", "5432")

# SQLAlchemy connection to the database
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
db = Session()


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
