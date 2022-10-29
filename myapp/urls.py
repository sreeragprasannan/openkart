
from django.urls import path, include
from .views import index,new_one,products,my_place,products_detail,add_products,update_products,delete_products

# app_name='myapp'
urlpatterns =[
    path('',index),
    path('new/',new_one),
    path('products/',products,name='products'),
    path('place/',my_place),
    path('products/<int:id>/',products_detail,name='products_details'),
    path('products/add',add_products,name='add_products'),
    path('products/update/<int:id>',update_products,name='update_products'),
    path('products/delete/<int:id>',delete_products,name='delete_products'),
    
]