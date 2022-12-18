from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from .category import Category, CategoryGender, CategoryColor, CategorySize


class Product(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='категория', null=True, blank=True)
    gender = models.ForeignKey(CategoryGender, on_delete=models.CASCADE, related_name='products', verbose_name='Категория по полу', null=True, blank=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование товара')
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)
    color = models.ForeignKey(CategoryColor, on_delete=models.CASCADE, related_name='products', default=None, verbose_name='Цвет', null=True, blank=True)
    size = models.ForeignKey(CategorySize, on_delete=models.CASCADE, related_name='products', default='All Size', verbose_name='Размер', null=True, blank=True)
    main_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='главное фото')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена', null=True, blank=True)
    available = models.BooleanField(default=True, verbose_name='доступный')
    created = models.DateTimeField(auto_now_add=True, verbose_name=' дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, related_name='photos',
                                verbose_name='product')
    images = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='фото')

    class Meta:
        ordering = ('product', 'images')
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self):
        return self.product.name
