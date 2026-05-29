from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path(
        '',
        include('accounts.urls')
    ),

    path(
        'dashboard/',
        include('security_engine.urls')
    ),

    path(
        'admin/',
        admin.site.urls
    ),

]