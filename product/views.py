from django.shortcuts import render
from django.views.generic import ListView,DetailView
from.models import Product,Brand,ProductImages,Review

# Create your views here.


class Productlist(ListView):
    model = Product



class ProductDetail(DetailView):
    model = Product



