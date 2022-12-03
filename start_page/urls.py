from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("summer", views.summer, name="summer"),
    path("winter", views.winter, name="winter"),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('show_cart', views.show_cart, name="show_cart")
]