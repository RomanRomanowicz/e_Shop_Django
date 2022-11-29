from django.db import models
from django.urls import reverse

from .category import Category, CategoryGender, CategoryColor, CategorySize


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='категория')
    gender = models.ForeignKey(CategoryGender, on_delete=models.CASCADE, related_name='products', verbose_name='Категория по полу')
    name = models.CharField(max_length=200, db_index=True, verbose_name='наименование товара')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='SLUG')
    color = models.ForeignKey(CategoryColor, on_delete=models.CASCADE, related_name='products', default=None, verbose_name='ЦВЕТ')
    size = models.ForeignKey(CategorySize, on_delete=models.CASCADE, related_name='products', default='All Size', verbose_name='РАЗМЕР')
    main_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='главное фото')
    image = models.ManyToManyField('Image', blank=True, related_name='photos', verbose_name='фото')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
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
    name = models.CharField(max_length=200, db_index=True, verbose_name='фото')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='фото')

    class Meta:
        ordering = ('name', 'image')
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self):
        return str(self.image)  # w przypadku pola z foto

    def get_absolute_url(self):
        return reverse('store:image_list')
