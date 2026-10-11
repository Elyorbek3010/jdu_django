# 3-HAFTA UCHUN UY VAZIFASI: Django modellari
**Kurs:** Introduction to Django  
**O'qituvchi:** Erkaboy Qadamboyev  
**Talaba:** Elyorbek  
**Jurnal raqami:** 28 (28 - 20 = 8-variant: Avtomobil bozori — `carmarket`)  

---

## Nazariy qism

### 1-topshiriq — Django ORM nima va u nima uchun kerak?

**Javob:**
> **Django ORM (Object-Relational Mapping)** — bu ma'lumotlar bazasi (masalan, SQLite, PostgreSQL, MySQL) bilan Python dasturlash tili o'rtasidagi ko'prik vazifasini bajaruvchi texnologiyadir.

**U nima uchun kerak va asosiy afzalliklari:**
1. **SQL yozmasdan bazani boshqarish:** Dasturchi qo'lda murakkab SQL so'rovlarini (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`) yozib o'tirmaydi. Buning o'rniga oddiy Python klasslari va metodlari bilan ishlaydi:
   - SQL: `INSERT INTO carmarket_car (brand, model, price) VALUES ('Chevrolet', 'Malibu', 28000);`
   - Django ORM: `Car.objects.create(brand='Chevrolet', model='Malibu', price=28000)`
2. **Xavfsizlik (SQL Injection himoyasi):** ORM barcha kiruvchi parametrlarni avtomatik tarzda tozalaydi va eng xavfli kiberhujumlardan biri bo'lgan SQL Injection'dan loyihani to'liq himoya qiladi.
3. **Ma'lumotlar bazasidan mustaqillik (Database Agnostic):** Agar ertaga loyihani SQLite'dan PostgreSQL yoki MySQL'ga ko'chirish kerak bo'lsa, kodni qayta yozish shart emas. Faqat `settings.py` faylida baza ulanish parametrini o'zgartirish kifoya, ORM kodlari o'zgarmaydi.
4. **O'qilishi oson va toza kod:** Python obyektlari bilan ishlash dasturchiga biznes mantiqqa ko'proq e'tibor qaratish imkonini beradi.

---

### 2-topshiriq — Migratsiyalar: `makemigrations` va `migrate` farqi

**Javob:**
Django'da migratsiya — bu `models.py` faylidagi Python klasslariga kiritilgan har qanday o'zgarishlarni ma'lumotlar bazasi jadvallariga xavfsiz va ketma-ketlikda ko'chirish mexanizmidir.

| Buyruq | Vazifasi | Ma'lumotlar bazasiga ta'siri |
| :--- | :--- | :--- |
| **`python manage.py makemigrations`** | `models.py` faylidagi yangi modellar yoki maydonlarni tahlil qilib, **migratsiya fayli (reja / blueprint)** yaratadi (masalan, `0001_initial.py`). | **Bazaga tegmaydi.** Faqat Python kodida o'zgarishlar rejasini xotirlab qo'yadi. |
| **`python manage.py migrate`** | Tayyorlangan migratsiya fayllarini o'qib chiqib, ma'lumotlar bazasida **haqiqiy SQL buyruqlarini bajaradi** (jadvallarni ochadi, ustunlarni qo'shadi yoki o'chiradi). | **Bazani o'zgartiradi.** Jadvallar va ma'lumotlar strukturasini yangilaydi. |

> **Hayotiy o'xshatish:**  
> - `makemigrations` — bu me'mor (arxitektor) tomonidan uy qurish uchun **chizma / reja chizilishi**.  
> - `migrate` — bu quruvchilar chizma asosida kelib, poydevor quyib **haqiqiy binoni qurishi**.

---

## Amaliy qism

### Talaba varianti ma'lumotlari:
- **Jurnal raqami:** 28
- **Variant hisobi:** 21-talabadan boshlab qayta 1-variantdan boshlanadi: `28 - 20 = 8`
- **Ilova nomi:** `carmarket`
- **Model nomi:** `Car`
- **Maydonlar:** `brand`, `model`, `price` (qo'shimcha: `year`)

---

### 3-topshiriq — Model yaratish

`carmarket/models.py` faylida quyidagi `Car` modeli yaratildi:

```python
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Markasi (Brand)")
    model = models.CharField(max_length=100, verbose_name="Modeli")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Narxi ($)")
    year = models.PositiveIntegerField(verbose_name="Ishlab chiqarilgan yili", null=True, blank=True)

    class Meta:
        verbose_name = "Avtomobil"
        verbose_name_plural = "Avtomobillar"

    def __str__(self):
        return f"{self.brand} {self.model} (${self.price})"
```

---

### 4-topshiriq — Migratsiya qilish

1. **Migratsiya rejasini yaratish:**
   ```powershell
   python manage.py makemigrations
   ```
   *Natija:* `carmarket\migrations\0001_initial.py` fayli hosil bo'ldi (`Create model Car`).

2. **Migratsiyani bazaga qo'llash:**
   ```powershell
   python manage.py migrate
   ```
   *Natija:* `Applying carmarket.0001_initial... OK` (bazada `carmarket_car` jadvali muvaffaqiyatli yaratildi).

---

### 5-topshiriq — Admin panelda boshqarish

1. **Modelni `admin.py` da ro'yxatdan o'tkazish:**
   `carmarket/admin.py` fayliga quyidagi kod yozildi:

   ```python
   from django.contrib import admin
   from .models import Car


   @admin.register(Car)
   class CarAdmin(admin.ModelAdmin):
       list_display = ('id', 'brand', 'model', 'price', 'year')
       search_fields = ('brand', 'model')
       list_filter = ('brand', 'year')
   ```

2. **Admin paneliga kirish uchun Superuser yaratildi:**
   - **Login:** `admin`
   - **Parol:** `admin123`

3. **Admin panel orqali qo'shilgan yozuvlar:**
   - **1-yozuv:** Chevrolet Malibu ($28,000.00, 2023-yil)
   - **2-yozuv:** Toyota Camry ($32,000.00, 2024-yil)
   - **3-yozuv:** BYD Song Plus ($29,000.00, 2024-yil)

---

## Darsda o'qituvchiga ko'rsatish tartibi:

1. **Terminalda loyihani ishga tushirish:**
   ```powershell
   cd d:\jdu_django\car_market
   python manage.py runserver
   ```
2. **Brauzerni ochish:**
   - [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) manziliga kiring.
   - Login: `admin`
   - Parol: `admin123`
3. **Ekranda ko'rsatish:**
   - **"Avtomobillar" (Cars)** bo'limini bosing.
   - Ekranda ro'yxatdan o'tgan Chevrolet Malibu, Toyota Camry, BYD Song Plus yozuvlarini ko'rsating.
   - Yuqoridagi **"Add Avtomobil +" (Avtomobil qo'shish)** tugmasini bosib, o'qituvchi oldida yana bir mashina kiritib ko'rsatishingiz mumkin.
4. **Kodni ko'rsatish:**
   - VS Code'da `carmarket/models.py` dagi `Car` klassini ochib ko'rsatish.
   - `carmarket/admin.py` dagi ro'yxatdan o'tkazish kodini ko'rsatish.
