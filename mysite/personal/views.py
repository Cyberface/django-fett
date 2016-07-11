from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """this is the home page"""
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me.','email@email.com']})
