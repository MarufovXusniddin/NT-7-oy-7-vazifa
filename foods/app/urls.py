from django.urls import path
from .views import (index, product_by_category, order_by_alphabet, order_by_alphabet_reverse,
                    order_by_price, discount, anotate, And)

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:id>/', product_by_category, name='product_by_category'),
    path('alphabet/', order_by_alphabet, name='alphabet'),
    path('alphabet_reverse/', order_by_alphabet_reverse, name='reverse'),
    path('price/', order_by_price, name='price'),
    path('discount/', discount, name='discount'),
    path('anotate/', anotate, name='anotate'),
    path('and/', And, name='and'),
]