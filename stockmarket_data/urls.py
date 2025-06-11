from django.urls import path

from .views import DeleteStockView, StocksListView

app_name = "stockmarket_data"

urlpatterns = [
    path("", StocksListView.as_view(), name="stocks_list"),
    path("delete/<int:pk>/", DeleteStockView.as_view(), name="delete_stock"),
]
