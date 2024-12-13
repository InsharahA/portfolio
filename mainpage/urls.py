from django.conf import settings
from django.db import router
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from django.http import HttpResponseNotFound
router = DefaultRouter()

router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
   path('api/', include(router.urls)),
   path('react/', views.react_view, name='react_page'),
    
]
