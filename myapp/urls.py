
from django.urls import path, include
from .views import index,products,products_detail,add_products,update_products,delete_products
from .views import ProductListView,ProductDetailView,ProductsUpdateView,ProductCreateView,ProductDeleteView

app_name='myapp'
urlpatterns =[
    path('',index),
    # path('new/',new_one),
    # path('products/',products,name='products'),
    path('products/',ProductListView.as_view(),name='products'),
    # path('place/',my_place),
    path('products/<int:pk>/',ProductDetailView.as_view(),name='products_details'),
    # path('products/add/',add_products,name='add_products'),
    path('products/add/',ProductCreateView.as_view(),name='add_products'),
    # path('products/update/<int:id>',update_products,name='update_products'),
    path('products/update/<int:pk>',ProductsUpdateView.as_view(),name='update_products'),
    # path('products/delete/<int:id>',delete_products,name='delete_products'),
    path('products/delete/<int:pk>',ProductDeleteView.as_view(),name='delete_products'),
    
]