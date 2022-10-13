
from django.urls import path, include
from .views import index,new_one,products,my_place

urlpatterns =[
    path('',index),
    path('new',new_one),
    path('products',products),
    path('place',my_place)
]