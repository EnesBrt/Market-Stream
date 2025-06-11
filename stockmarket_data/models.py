from django.db import models


class StockMarketData(models.Model):
    stock_symbol = models.CharField(max_length=100)
    from_date = models.DateTimeField()
    after_hours = models.FloatField()
    at_close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    at_open = models.FloatField()
    pre_market = models.FloatField()
    status = models.CharField(max_length=100)
    volume = models.FloatField()
    otc = models.BooleanField(null=True, blank=True)
    sma = models.FloatField()
    ema = models.FloatField()
    macd = models.FloatField()
    rsi = models.FloatField()

    def __str__(self):
        return f"{self.stock_symbol} - {self.from_date}"


class SearchStorage(models.Model):
    stock_id = models.ForeignKey(StockMarketData, on_delete=models.CASCADE)
