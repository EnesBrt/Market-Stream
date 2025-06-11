import uvicorn
from database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.news_router import news_router
from routers.stock_router import stock_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Market Stream REST APT",
    description="REST API crud for news data and stocks data",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news_router)
app.include_router(stock_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Martket Stream REST API !",
        "documentation": "http://localhost:8001/docs",
    }


@app.get("/status")
async def status_check():
    return {"status": "running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
