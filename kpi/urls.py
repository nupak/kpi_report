from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('idef0/', views.method_calculating, name="idef"),
    path('dragon/', views.method_calculating, name="dragon"),
]
