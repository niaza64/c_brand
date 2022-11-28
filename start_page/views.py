from django.shortcuts import render
from django.http import HttpResponse
from .models import cloth
# Create your views here.
def index(request):
    return render(request, "start_page/index.html")

def summer(request):
    return render(request, "start_page/summer.html", {
        "cloths": cloth.objects.all()
    }
    )

def winter(request):
    return render(request, "start_page/winter.html")