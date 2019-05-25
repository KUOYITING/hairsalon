from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('', views.hairsalon, name='hairsalon'),
    path('indexbooking/', views.indexbooking, name='indexbooking'),
]