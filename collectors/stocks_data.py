from polygon import RESTClient

from .database import StockMarketData, db

# date = input("Enter a valid date in YYYY-MM-DD format: ")

# stock_symbol = input("Enter a valid stock symbol: ")

client = RESTClient("qxEhMjxem7qWLGVy28wLB2Cvi6sUM_dv")


def get_stock_data_from_api(stock_symbol, date):
    request = client.get_daily_open_close_agg(
        stock_symbol,
        date,
        adjusted="true",
    )

    ema = client.get_ema(
        ticker=stock_symbol,
        timespan="day",
        adjusted="true",
        window="50",
        series_type="close",
        order="desc",
        limit="1",
    )

    ema = ema.values[0].value

    sma = client.get_sma(
        ticker=stock_symbol,
        timespan="day",
        adjusted="true",
        window="50",
        series_type="close",
        order="desc",
        limit="1",
    )

    sma = sma.values[0].value

    macd = client.get_macd(
        ticker=stock_symbol,
        timespan="day",
        adjusted="true",
        short_window="12",
        long_window="26",
        signal_window="9",
        series_type="close",
        order="desc",
        limit="1",
    )

    macd = macd.values[0].value

    rsi = client.get_rsi(
        ticker=stock_symbol,
        timespan="day",
        adjusted="true",
        window="14",
        series_type="close",
        order="desc",
        limit="1",
    )

    rsi = rsi.values[0].value

    return request, ema, sma, macd, rsi


def add_stock_data_to_db(stock_symbol, request, ema, sma, macd, rsi):
    stock_data = {
        "stock_symbol": stock_symbol,
        "from_date": request.from_,
        "after_hours": request.after_hours,
        "at_close": request.close,
        "high": request.high,
        "low": request.low,
        "at_open": request.open,
        "pre_market": request.pre_market,
        "status": request.status,
        "volume": request.volume,
        "otc": request.otc,
        "sma": sma,
        "ema": ema,
        "macd": macd,
        "rsi": rsi,
    }

    stock_data = StockMarketData(**stock_data)
    db.add(stock_data)
    db.commit()


if __name__ == "__main__":
    request, ema, sma, macd, rsi = get_stock_data_from_api()
    add_stock_data_to_db(request, ema, sma, macd, rsi)
