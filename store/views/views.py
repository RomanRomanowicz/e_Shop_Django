from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from store.models.products import Product


class HomePageView(ListView):
    model = Product
    context_object_name = 'home'
    template_name = 'store/base.html'