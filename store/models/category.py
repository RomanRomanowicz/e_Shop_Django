from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='наименование категории')
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class CategoryGender(models.Model):
    gender = models.CharField(max_length=200, db_index=True, blank=True, null=True, verbose_name='Категория по полу')
    slug = AutoSlugField(populate_from='gender', unique=True, null=True, default=None)

    class Meta:
        ordering = ('gender',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория по полу'

    def __str__(self):
        return self.gender


class CategoryColor(models.Model):
    color = models.CharField(max_length=200, db_index=True, verbose_name='Категория по цвету')
    slug = AutoSlugField(populate_from='color', unique=True, null=True, default=None)

    class Meta:
        ordering = ('color',)
        verbose_name = 'Категория по цвету'
        verbose_name_plural = 'Категория по цвету'

    def __str__(self):
        return self.color


class CategorySize(models.Model):
    size = models.CharField(max_length=200, db_index=True, verbose_name='Категория по размеру')
    slug = AutoSlugField(populate_from='size', unique=True, null=True, default=None)

    class Meta:
        ordering = ('size',)
        verbose_name = 'Категория по размеру'
        verbose_name_plural = 'Категория по размеру'

    def __str__(self):
        return self.size