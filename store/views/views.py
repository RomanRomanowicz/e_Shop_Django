from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from cart.forms import CartAddProductForm
from store.filters import ProductFilter
from store.forms import *
from store.models.products import Product
from django.contrib import messages


class HomePageView(ListView):
    model = Product
    context_object_name = 'home'
    template_name = 'store/home.html'


def shop_view(request):
    # products = Product.objects.all()
    products = Product.objects.filter(available=True)
    products_filter = ProductFilter(request.GET, queryset=products)
    context = {'products_filter': products_filter, 'products': products}
    return render(request, 'store/shop.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    images = Image.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/detail.html', {'product': product,"images": images, 'cart_product_form': cart_product_form})


def create_product(request):
    productform = ProductForm()
    imageform = ImageForm()
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        productform = ProductForm(request.POST, request.FILES)
        if productform.is_valid():
            product = productform.save(commit=False)
            product.vendor = request.user
            product.save()
            messages.success(request, "Product created successfully")
            for file in files:
                Image.objects.create(product=product, images=file)
            return redirect("home")
    context = {"p_form": productform, "i_form": imageform}
    return render(request, "store/create.html", context)