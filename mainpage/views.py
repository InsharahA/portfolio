import logging
import os
from django.conf import settings
from django.shortcuts import render, redirect


# Create your views here.

def mainpage(request):
    folder_path = os.path.join(settings.BASE_DIR, 'mainpage','static', 'images', 'Skills')
    
    files = []
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return render(request, 'mainpage/mainpage.html', {'files': files})

def about(request):
    return render(request, 'mainpage/about.html')

def info(request):
    
    return render(request, 'mainpage/info.html', {})

