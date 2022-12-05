from django.db import models
from django.conf import settings
# Create your models here.
class cloth(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    count = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

CART_SESSION_ID = 'cart2'

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def get_cart_list(self):
        """
        Returns the cart as a list, this format is more suitable than a dictionary for
        the frontend to make a detail view with.
        """
        cart_list = []
    

        for name, val in self.cart.items():
            cart_list.append({
                "name": name,
                "price": val['price'],
                "quantity": val['quantity'],
            })
        return cart_list
   
    def add(self, product):
        if product.name not in self.cart:
            self.cart[product.name] = {'quantity': 0, 'price':str(product.price)}
        self.cart[product.name]['quantity'] += 1
        self.save()
        print(self.cart)

    def save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def get_total_price(self):
        total = 0
        for name, val in self.cart.items():
            total += int(val['quantity']) * int(val['price'])
        print("dasdafsdfasfasfasdfw csx")
        return total