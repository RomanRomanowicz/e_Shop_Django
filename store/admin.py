from django.contrib import admin

from store.models.category import *
from store.models.products import *

# Register your models here.

admin.site.register([Category, CategoryGender, CategoryColor, CategorySize])
admin.site.register([Product, Image])