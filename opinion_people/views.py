from django.shortcuts import render

# Create your views here.
from opinion_people.models import Restaurant, Dish
from opinion_people.serializers import RestaurantSerializer, DishSerializer
from rest_framework import viewsets

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

