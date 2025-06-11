import requests

from collectors.database import StockMarketNews, db

# Data collection from the API alphavantage
url = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&sort=LATEST&limit=100&apikey=OGP1J9635MRFC8TI"


def get_news_data_from_api(url):
    r = requests.get(url, timeout=30)
    data = r.json()
    return data


def add_news_data_to_db(data):
    for news in data["feed"]:
        news_data = {
            "title": news["title"],
            "url": news["url"],
            "time_published": news["time_published"],
            "authors": news["authors"],
            "summary": news["summary"],
            "banner_image": news["banner_image"],
            "source": news["source"],
            "overall_sentiment_label": news["overall_sentiment_label"],
            "overall_sentiment_score": news["overall_sentiment_score"],
        }
        news_data = StockMarketNews(**news_data)
        db.add(news_data)
        db.commit()
        print(f"News data added: {news_data['title']}")


if __name__ == "__main__":
    try:
        print("Script started")
        data = get_news_data_from_api(url)
        add_news_data_to_db(data)
    except Exception as e:
        print(f"Errorr: {e}")
    finally:
        print("🔚 closing DB")
        db.close()
