from django.urls import path, include
from .views import register
from django.contrib.auth import views as authentication_views

app_name = 'users'

urlpatterns =[
    path('register/',register, name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout')
    # path('products/',products,name='products'),
    # path('products/<int:id>/',products_detail,name='products_details'),
    # path('products/add',add_products,name='add_products'),
    # path('products/update/<int:id>',update_products,name='update_products'),
    # path('products/delete/<int:id>',delete_products,name='delete_products'),
    
]