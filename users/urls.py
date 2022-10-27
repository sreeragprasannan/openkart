from django.urls import path, include
from .views import register

urlpatterns =[
    path('register/',register, name='register'),
    # path('products/',products,name='products'),
    # path('products/<int:id>/',products_detail,name='products_details'),
    # path('products/add',add_products,name='add_products'),
    # path('products/update/<int:id>',update_products,name='update_products'),
    # path('products/delete/<int:id>',delete_products,name='delete_products'),
    
]