
from django.urls import path, include
from .views import index,new_one,products,my_place,products_detail,add_products

urlpatterns =[
    path('',index),
    path('new/',new_one),
    path('products/',products,name='products'),
    path('place/',my_place),
    path('products/<int:id>/',products_detail,name='products_details'),
    path('products/add',add_products)
]