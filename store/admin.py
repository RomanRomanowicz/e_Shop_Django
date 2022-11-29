from django.contrib import admin
from store.models.products import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('image', )


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    # inlines = ImageInline


admin.site.register(Image, ImageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


@admin.register(CategoryGender)
class CategoryGenderAdmin(admin.ModelAdmin):
    list_display = ('gender', 'slug')
    prepopulated_fields = {"slug": ("gender", )}


@admin.register(CategoryColor)
class CategoryColorAdmin(admin.ModelAdmin):
    list_display = ('color', 'slug')
    prepopulated_fields = {"slug": ("color", )}


@admin.register(CategorySize)
class CategorySizeAdmin(admin.ModelAdmin):
    list_display = ('size', 'slug')
    prepopulated_fields = {"slug": ("size", )}