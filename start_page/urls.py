from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("summer", views.summer, name="summer"),
    path("winter", views.winter, name="winter"),
    path('update/<str:name>', views.update, name='update')
]