from django.db import models


# Create your models here.
class StockMarketNews(models.Model):
    title = models.CharField(max_length=10000)
    summary = models.TextField(max_length=10000)
    banner_image = models.URLField(max_length=10000, blank=True, null=True)
    authors = models.CharField(max_length=10000)
    time_published = models.DateTimeField(max_length=10000)
    source = models.CharField(max_length=10000)
    overall_sentiment_label = models.CharField(max_length=10000)
    overall_sentiment_score = models.FloatField(max_length=10000)
    url = models.URLField(max_length=10000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Stock Market News"
        verbose_name_plural = "Stock Market News"
