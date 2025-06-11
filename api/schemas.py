from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel

"""
Schemas for the news REST API
"""


class News(BaseModel):
    title: str
    summary: str
    banner_image: str
    authors: str
    time_published: datetime
    source: str
    overall_sentiment_label: str
    overall_sentiment_score: float
    url: str


class NewsResponse(News):
    id: int

    class Config:
        from_attributes = True


"""
Schemas for the stocks REST API
"""


class Stock(BaseModel):
    stock_symbol: str
    from_date: datetime
    after_hours: float
    at_close: float
    high: float
    low: float
    at_open: float
    pre_market: float
    status: str
    volume: float
    otc: Union[bool, None] = None
    sma: float
    ema: float
    macd: float
    rsi: float


class StockCreate(Stock):
    pass


class StockUpdate(BaseModel):
    stock_symbol: Optional[str] = None
    from_date: Optional[datetime] = None
    after_hours: Optional[float] = None
    at_close: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    at_open: Optional[float] = None
    pre_market: Optional[float] = None
    status: Optional[str] = None
    volume: Optional[float] = None
    otc: Union[bool, None] = None
    sma: Optional[float] = None
    ema: Optional[float] = None
    macd: Optional[float] = None
    rsi: Optional[float] = None


class StockResponse(Stock):
    id: int

    class Config:
        from_attributes = True
