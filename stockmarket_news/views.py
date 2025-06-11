from django.shortcuts import render
from django.views.generic import ListView

from .models import StockMarketNews


class NewsListView(ListView):
    model = StockMarketNews
    context_object_name = "news"
    template_name = "news_page.html"
    queryset = StockMarketNews.objects.order_by("-time_published")
