from database import db
from fastapi import APIRouter, HTTPException
from models import StockMarketData
from schemas import Stock, StockCreate, StockResponse, StockUpdate

stock_router = APIRouter()


# get all stocks
@stock_router.get("/stocks", response_model=list[StockResponse])
async def get_all_stocks(skip: int = 0, limit: int = 10):
    stocks = db.query(StockMarketData).offset(skip).limit(limit).all()
    return stocks


# get a specific stock by id
@stock_router.get("/stocks/{stock_id}", response_model=StockResponse)
def get_id_stock(stock_id: int):
    stock = db.query(StockMarketData).filter(StockMarketData.id == stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock


# create a new stock
@stock_router.post("/create_stock", response_model=StockResponse)
async def create_stock(stock: StockCreate):
    new_stock = StockMarketData(**stock.model_dump())
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock


# update a stock
@stock_router.put("/update_stock/{stock_id}", response_model=StockResponse)
async def update_stock(stock_id: int, stock: StockUpdate):
    stock_to_update = (
        db.query(StockMarketData).filter(StockMarketData.id == stock_id).first()
    )
    if not stock_to_update:
        raise HTTPException(status_code=404, detail="Stock not found")

    for key, value in stock.model_dump(exclude_unset=True).items():
        if hasattr(stock_to_update, key):
            setattr(stock_to_update, key, value)

    db.commit()
    db.refresh(stock_to_update)

    return stock_to_update


# delete a stock
@stock_router.delete("/delete_stock/{stock_id}", response_model=StockResponse)
async def delete_stock(stock_id: int):
    stock_to_delete = (
        db.query(StockMarketData).filter(StockMarketData.id == stock_id).first()
    )
    if not stock_to_delete:
        raise HTTPException(status_code=404, detail="Stock not found")
    db.delete(stock_to_delete)
    db.commit()
    return stock_to_delete
