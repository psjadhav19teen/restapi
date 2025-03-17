"""
URL configuration for productproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from app.views import AllProductview,AddProduct,UpdateProduct,DeleteProduct
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.Apioverview,name="Apioverview"),
    path('AllProductview/',AllProductview.as_view(),name='AllProductview'),
    path('AddProduct/',AddProduct.as_view(),name='AddProduct'),
    path('UpdateProduct/update/<int:pk>/',UpdateProduct.as_view(),name='UpdateProduct'),
    path('DeleteProduct/delete/<int:pk>/',DeleteProduct.as_view(),name='DeleteProduct'),
    path('searchbycategory/',views.searchbycategory,name='searchbycategory')

]
