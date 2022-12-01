from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import cloth
from django.urls import reverse
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

def add_to_cart(request, name):
    cclothtype = cloth.objects.get(name=name)
    clothtype.count -=  1
    clothtype.save()
    return HttpResponseRedirect(reverse('summer'))

