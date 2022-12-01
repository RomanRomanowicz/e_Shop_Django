from django.shortcuts import render
from django.views.generic import ListView, CreateView
from store.models.products import Product


class DashboardView(ListView):
    model = Product
    context_object_name = 'dashboard'
    template_name = 'dashboard/dashboard.html'


class CreateProduct(CreateView):
    model = Product
    context_object_name = 'create'
    template_name = 'dashboard/create.html'