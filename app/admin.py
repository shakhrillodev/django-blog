from django.contrib import admin
from .models import Category, News, Region

# Register your models here.
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Region)
