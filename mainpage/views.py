from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage/mainpage.html', {})

def about(request):
    return render(request, 'mainpage/about.html')
