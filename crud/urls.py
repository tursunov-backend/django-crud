from django.urls import path

from .views import items_view, item_one_view


urlpatterns = [
    path('items/', items_view, name='items'), # base/api/items/ -> GET, POST
    path('items/<int:id>', item_one_view, name='one_item'),
]
