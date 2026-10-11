# 12-HAFTA UCHUN UY VAZIFASI: Django REST Framework (DRF)
**Kurs:** Introduction to Django  
**O'qituvchi:** Erkaboy Qadamboyev  
**Talaba:** Elyorbek  
**Jurnal raqami:** 28 (28 - 20 = 8-variant: Avtomobil bozori — `carmarket` / Model: `Car`)  

---

## Nazariy qism (1–2-topshiriq)

### 1-topshiriq — API nima va u nima uchun kerak?
**Javob:**
> **API (Application Programming Interface — Ilovalar dasturlash interfeysi)** — bu turli xil dasturlar, xizmatlar yoki tizimlarning o'zaro ma'lumot almashishi va aloqa qilishi uchun mo'ljallangan qoidalar, protokollar hamda vositalar to'plamidir.
> 
> **U nima uchun kerak:** API orqali server (backend) frontend (veb-sayt, Android / iOS mobil ilovalar, desktop dasturlar) bilan standart formatda (masalan, JSON) ma'lumot almashadi. Natijada bir xil backend ma'lumotlarini bir vaqtning o'zida ham veb-saytga, ham mobil ilovaga uzatish, shuningdek uchinchi tomon tizimlari bilan xavfsiz integratsiya qilish imkoni yaratiladi.

---

### 2-topshiriq — Serializer nima vazifani bajaradi?
**Javob:**
> **Serializer (Serializator)** — Django REST Framework'da murakkab ma'lumotlar turlarini (Django ORM modellari va QuerySet'larni) osonlik bilan JSON, XML kabi frontend tushunadigan formatga aylantirib beruvchi (**Serialization**) vositadir.
> 
> Shuningdek, u teskari jarayonni ham bajaradi (**Deserialization**): mijozdan (klientdan) kelayotgan JSON ma'lumotlarini qabul qilib, ularning to'g'riligini tekshiradi (validatsiya qiladi) va ma'lumotlar bazasiga saqlash uchun Python obyektlariga o'giradi.

---

## Amaliy qism (3–5-topshiriq)

### Talaba varianti ma'lumotlari:
- **Jurnal raqami:** 28
- **Variant:** `28 - 20 = 8`
- **Ilova (app) nomi:** `carmarket`
- **Model nomi:** `Car`
- **Maydonlar:** `brand`, `model`, `price` (qo'shimcha: `year`, `category`, `image`)

---

### 3-topshiriq — DRF o'rnatish va sozlash

1. **Kutubxonani o'rnatish:**
   ```powershell
   pip install djangorestframework
   ```

2. **`config/settings.py` fayliga qo'shish:**
   `INSTALLED_APPS` ro'yxatiga `'rest_framework'` qo'shildi:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       # Loyiha ilovalari
       'carmarket',
       # Django REST Framework
       'rest_framework',
   ]
   ```

---

### 4-topshiriq — Serializer va ViewSet yaratish

1. **Serializer yaratish (`carmarket/serializers.py`):**
   `Car` modeli uchun `ModelSerializer` yaratildi:
   ```python
   from rest_framework import serializers
   from .models import Car


   class CarSerializer(serializers.ModelSerializer):
       class Meta:
           model = Car
           fields = '__all__'
   ```

2. **ModelViewSet yaratish (`carmarket/views.py`):**
   `CarViewSet` klassi yaratildi:
   ```python
   from rest_framework import viewsets
   from .serializers import CarSerializer


   class CarViewSet(viewsets.ModelViewSet):
       queryset = Car.objects.all()
       serializer_class = CarSerializer
   ```

---

### 5-topshiriq — Router sozlash va API'ni sinash

1. **Router orqali endpoint yaratish (`carmarket/urls.py`):**
   ```python
   from django.urls import path, include
   from rest_framework.routers import DefaultRouter
   from .views import CarViewSet, ...

   router = DefaultRouter()
   router.register('carmarket', CarViewSet, basename='carmarket')

   urlpatterns = [
       ...,
       # API endpointlari
       path('api/', include(router.urls)),
   ]
   ```

2. **API manzillari:**
   - Asosiy API yo'nalishi: `http://127.0.0.1:8000/api/`
   - Barcha mashinalar ro'yxati (List) va yangi qo'shish (Create):  
     `http://127.0.0.1:8000/api/carmarket/`
   - Bitta obyektni ko'rish (Detail), o'zgartirish (Update) va o'chirish (Delete):  
     `http://127.0.0.1:8000/api/carmarket/1/`

---

## O'qituvchiga ko'rsatish va sinash tartibi

1. **Serverni ishga tushirish:**
   ```powershell
   cd d:\jdu_django\car_market
   python manage.py runserver
   ```

2. **Brauzerda tekshirish:**
   - Ro'yxatni ko'rish: `http://127.0.0.1:8000/api/carmarket/` (DRF Browsable API ochiladi, JSON ro'yxat va pastida yangi mashina qo'shish formasi ko'rinadi).
   - Alohida mashinani ko'rish: `http://127.0.0.1:8000/api/carmarket/1/` (ID=1 bo'lgan avtomobil ma'lumotlari, PUT/DELETE tugmalari ko'rinadi).

3. **Testlarni ishga tushirish:**
   ```powershell
   python manage.py test carmarket
   ```
