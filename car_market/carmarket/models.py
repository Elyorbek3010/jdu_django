from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brend nomi")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Mamlakat")

    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='cars')
    brand = models.CharField(max_length=100, verbose_name="Markasi (Brand)")
    brand_ref = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='cars', verbose_name="Brend ma'lumoti")
    model = models.CharField(max_length=100, verbose_name="Modeli")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Narxi ($)")
    year = models.PositiveIntegerField(verbose_name="Ishlab chiqarilgan yili", null=True, blank=True)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)

    class Meta:
        verbose_name = "Avtomobil"
        verbose_name_plural = "Avtomobillar"

    def __str__(self):
        return f"{self.brand} {self.model} (${self.price})"


class Listing(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='listings', verbose_name="Avtomobil")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings', verbose_name="E'lon muallifi", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="E'lon sarlavhasi")
    description = models.TextField(verbose_name="Batafsil tavsif", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    is_active = models.BooleanField(default=True, verbose_name="Faol e'lon")

    class Meta:
        verbose_name = "E'lon (Listing)"
        verbose_name_plural = "E'lonlar (Listings)"

    def __str__(self):
        return self.title
