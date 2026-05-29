from django.contrib import admin
from django.urls import path
from security_engine.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]