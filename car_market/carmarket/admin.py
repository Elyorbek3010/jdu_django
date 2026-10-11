from django.contrib import admin
from .models import Car, Category, Brand, Listing


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'price', 'year')
    search_fields = ('brand', 'model')
    list_filter = ('brand', 'year')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name',)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'car', 'author', 'created_at', 'is_active')
    search_fields = ('title', 'car__brand', 'car__model')
    list_filter = ('is_active', 'created_at')


admin.site.register(Category)


