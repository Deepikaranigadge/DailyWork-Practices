from django.urls import path
from .views import *

urlpatterns = [
     #Other URL pattrens
     path("add-to-cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
     path('cart/count/', cart_count, name='cart_count'),
     path('cart/', cart_view, name='cart'),
     path('cart/remove/<int:cart_item_id>/',
          remove_from_cart, name='remove_from_cart'),
          path('checkout/', checkout_view, name='checkout'),
          path('orders/', orders_view, name='orders'),
]
