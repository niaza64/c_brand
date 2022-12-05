from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import cloth, Cart
from django.urls import reverse

def index(request):
    return render(request, "start_page/index.html")

def summer(request):
    return render(request, "start_page/summer.html", {
        "cloths": cloth.objects.all()
    }
    )

def winter(request):
    return render(request, "start_page/winter.html")

def show_cart(request):
    cart = Cart(request).get_cart_list
    pr = Cart(request).get_total_price
    print(cart)
    print("lohgfhdfl", pr)
    return render(request, "start_page/cart.html", {
        "cart": cart,
        "pr": pr,
    })

def add_to_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(cloth, id=id)
    cart.add(product=product)
    return HttpResponseRedirect(reverse('summer'))

