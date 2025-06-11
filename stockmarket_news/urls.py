from django.urls import path

from .views import NewsListView

app_name = "stockmarket_news"

urlpatterns = [
    path("", NewsListView.as_view(), name="news_list"),
]
