"""mylibrary_ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from library import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index page'),
    path('login',views.login,name='login page'),
    path('register',views.register,name='register page'),
    path('logout',views.logout,name='logout page'),
    path('myprofile',views.myprofile,name='logout page'),
    path('update',views.update_book,name='logout page'),
    path('addbook',views.addbook,name='logout page'),
    path('getall',views.getallbooks,name='logout page'),
    path('delete',views.delete_book,name='logout page'),
]
