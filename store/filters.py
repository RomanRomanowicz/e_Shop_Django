import django_filters
from store.models.products import Product


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ['category', 'gender', 'color', 'size']