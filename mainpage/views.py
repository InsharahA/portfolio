import logging
import os
from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

def mainpage(request):
    folder_path = os.path.join(settings.BASE_DIR, 'mainpage','static', 'images', 'Skills')
    context = {
        'static_url': settings.STATIC_URL,
    }
    files = []
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return render(request, 'mainpage/mainpage.html',{'files': files, 'static_url': settings.STATIC_URL})

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
def react_view(request):
    # Pass STATIC_URL to the React template
    context = {'static_url': settings.STATIC_URL}
    return render(request, 'mainpage.html', context)
