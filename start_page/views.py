from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "start_page/index.html")

def summer(request):
    return render(request, "start_page/summer.html")

def winter(request):
    return render(request, "start_page/winter.html")