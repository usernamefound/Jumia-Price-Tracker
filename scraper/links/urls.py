from django.urls import path
from .views import price_tracker, DeleteItem, update_prices

app_name = 'links'
urlpatterns = [
    path('', price_tracker, name='tracker'),
    path('delete/<int:pk>/', DeleteItem.as_view(), name='deleteitem'),
    path('update/', update_prices, name='refresh-prices'),
]