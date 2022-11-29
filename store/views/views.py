from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from cart.forms import CartAddProductForm
from store.filters import ProductFilter
from store.models.products import Product


class HomePageView(ListView):
    model = Product
    context_object_name = 'home'
    template_name = 'store/base.html'


def shop_view(request):
    # products = Product.objects.all()
    products = Product.objects.filter(available=True)
    products_filter = ProductFilter(request.GET, queryset=products)
    context = {'products_filter': products_filter, 'products': products}
    return render(request, 'store/shop.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/detail.html', {'product': product, 'cart_product_form': cart_product_form})