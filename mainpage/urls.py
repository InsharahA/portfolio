from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    
]