"""djangoecomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from core import views
#from core.views import index, contact, product, product_list

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name= 'contact'),
    path('produto/', views.product, name='produto'),
    path('produtos/', views.product_list, name='product_list'),
    path('warning/', views.warning, name='warning'),
    path('termos/', views.about, name='about'),
    path('admin/', admin.site.urls),
]
