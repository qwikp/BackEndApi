from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Cart,CartItem
from . import serializers

class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer

class CartItemViewset(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = serializers.CartItemSerializer
