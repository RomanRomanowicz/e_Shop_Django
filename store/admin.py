from django.contrib import admin
from store.models.products import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}


class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'images')
    # inlines = ImageInline


admin.site.register(Image, ImageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


@admin.register(CategoryGender)
class CategoryGenderAdmin(admin.ModelAdmin):
    list_display = ('gender', )
    # prepopulated_fields = {"slug": ("gender", )}


@admin.register(CategoryColor)
class CategoryColorAdmin(admin.ModelAdmin):
    list_display = ('color', )
    # prepopulated_fields = {"slug": ("color", )}


@admin.register(CategorySize)
class CategorySizeAdmin(admin.ModelAdmin):
    list_display = ('size', )
    # prepopulated_fields = {"slug": ("size", )}