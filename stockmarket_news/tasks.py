import logging

from celery import shared_task

from collectors.news_extract_load import add_news_data_to_db, get_news_data_from_api
from stockmarket_news.models import StockMarketNews

logger = logging.getLogger(__name__)


@shared_task(name="get_news")
def get_news():
    logger.info("Executing get_news task")
    # delete all news from the database from the last data collection
    StockMarketNews.objects.all().delete()
    # get the news from the api
    url = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&sort=LATEST&limit=100&apikey=OGP1J9635MRFC8TI"
    data = get_news_data_from_api(url)
    add_news_data_to_db(data)
    logger.info("News data added to database")
