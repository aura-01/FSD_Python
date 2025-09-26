"""
URL configuration for e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from website.api import views 
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    # Token authentication endpoint
    path('token/', drf_views.obtain_auth_token, name='api_token_auth'),
    #only api urls are here
    path('products/', views.product_list, name='product_list'), 
    #path('/products/<int:product_id>/', views.product_detail, name='product_detail'),   
    #path('/customers/', views.customer_list, name='customer_list'),
    #path('/customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    #path('/orders/', views.order_list, name='order_list'),  
]
