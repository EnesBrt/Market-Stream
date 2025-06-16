from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from collectors.stocks_data import add_stock_data_to_db, get_stock_data_from_api

from .models import SearchStorage, StockMarketData


class StocksListView(ListView):
    model = SearchStorage  # Afficher les recherches persistantes
    context_object_name = "stocks"
    template_name = "stocks_page.html"
    ordering = ["-id"]  # Plus récents en premier

    def get_queryset(self):
        query = self.request.GET.get("q")  # stock symbol
        date = self.request.GET.get("date")  # date

        # Si on fait une recherche (les deux champs remplis)
        if query and date:
            try:
                # Appeler l'API pour récupérer de nouvelles données
                request, ema, sma, macd, rsi = get_stock_data_from_api(query, date)
                add_stock_data_to_db(query, request, ema, sma, macd, rsi)
                stock_search = StockMarketData.objects.filter(
                    stock_symbol=query, from_date=date
                )
                if stock_search.exists():
                    # Ajouter à l'historique persistant avec l'utilisateur connecté
                    if self.request.user.is_authenticated:
                        SearchStorage.objects.create(
                            stock_id=stock_search.first(),
                            user_id=self.request.user
                        )
            except Exception as e:
                print(f"Erreur API (rate limit?): {e}")

        # Filtrer les résultats par utilisateur connecté
        if self.request.user.is_authenticated:
            return SearchStorage.objects.filter(user_id=self.request.user).order_by("-id")
        else:
            # Pour les utilisateurs non connectés, retourner une queryset vide
            return SearchStorage.objects.none()


class DeleteStockView(View):
    def post(self, request, pk):
        # Supprimer un résultat spécifique seulement si il appartient à l'utilisateur connecté
        try:
            if request.user.is_authenticated:
                search_item = SearchStorage.objects.get(pk=pk, user_id=request.user)
                search_item.delete()
            else:
                return redirect("stockmarket_data:stocks_list")
        except SearchStorage.DoesNotExist:
            return "No data found"
        return redirect("stockmarket_data:stocks_list")
