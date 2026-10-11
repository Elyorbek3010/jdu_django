# 13-HAFTA UCHUN UY VAZIFASI: Django’da testlash
**Kurs:** Introduction to Django  
**O'qituvchi:** Erkaboy Qadamboyev  
**Talaba:** Elyorbek  
**Jurnal raqami:** 28 (28 - 20 = 8-variant: Avtomobil bozori — `carmarket` / Model: `Car`)  

---

## Nazariy qism (1–2-topshiriq)

### 1-topshiriq — Nima uchun test yozamiz?
**Javob:**
> Test yozish dastur sifatini va barqarorligini ta'minlashning eng asosiy vositasidir.
> 
> **Asosiy afzalliklari:**
> 1. **Regressiya va xatolarning oldini olish (Xavfsiz refaktoring):** Kodga yangi xususiyatlar qo'shilganda yoki mavjud kod optimallashtirilganda, tizimning avvalgi ishlayotgan qismlari buzilib qolmaganligini avtomatik kafolatlaydi.
> 2. **Vaqtni tejash va yuqori ishonchlilik:** Har bir o'zgarishdan so'ng saytni brauzerda qayta-qayta qo'lda tekshirish o'rniga, bir necha soniya ichida yuzlab testlarni ishga tushirib butun loyihaning to'g'ri ishlayotganiga ishonch hosil qilish mumkin.

---

### 2-topshiriq — pytest asoslari: `@pytest.mark.django_db` va `assert`
**Javob:**
> - **`@pytest.mark.django_db`:** Bu maxsus pytest dekoratori bo'lib, test funksiyasiga Django'ning test ma'lumotlar bazasiga (SQLite in-memory/test DB) kirish va u bilan ishlash (obyekt yaratish, o'qish, yangilash) ruxsatini beradi. Agar ushbu dekorator qo'yilmasa, bazaga murojaat qilganda `DatabaseAccessDenied` xatosi yuz beradi.
> - **`assert`:** Bu Python'ning kutilgan natija bilan haqiqiy natijani solishtirish operatoridir. Agar berilgan ifoda to'g'ri (`True`) bo'lsa, test muvaffaqiyatli davom etadi; agar noto'g'ri (`False`) bo'lsa, test to'xtaydi va pytest aynan qaysi qiymatlar mos kelmaganini ko'rsatib xatolik (`AssertionError`) beradi.

---

## Amaliy qism (3–5-topshiriq)

### Talaba varianti ma'lumotlari:
- **Jurnal raqami:** 28
- **Variant:** `28 - 20 = 8`
- **Ilova (app) nomi:** `carmarket`
- **Model nomi:** `Car`
- **Maydonlar:** `brand`, `model`, `price` (qo'shimcha: `year`)

---

### 3-topshiriq — pytest sozlash

1. **Paketlarni o'rnatish:**
   ```powershell
   pip install pytest pytest-django
   ```

2. **Loyiha ildizida `pytest.ini` fayli yaratildi:**  
   Fayl yo'li: `car_market/pytest.ini`
   ```ini
   [pytest]
   DJANGO_SETTINGS_MODULE = config.settings
   python_files = tests.py test_*.py *_tests.py
   ```

---

### 4-topshiriq — Model uchun test yozish

`carmarket/test_models.py` faylida `@pytest.mark.django_db` dekoratori va `assert` operatori yordamida `Car` modeli tekshirildi:

```python
import pytest
from carmarket.models import Car


@pytest.mark.django_db
def test_car_model():
    # 1. Bitta obyekt yaratish
    car = Car.objects.create(
        brand="BMW",
        model="M5",
        price=95000.00,
        year=2023,
    )

    # 2. Assert bilan maydonini tekshirish
    assert car.brand == "BMW"
    assert car.model == "M5"
    assert car.price == 95000.00
```

---

### 5-topshiriq — View uchun test va ishga tushirish

1. **`carmarket/test_views.py` faylida test yozildi:**  
   `client` fixture yordamida ro'yxat ko'rsatuvchi view (`CarListView`) chaqirilib, HTTP status kodi tekshirildi:

```python
import pytest
from django.urls import reverse
from carmarket.models import Car


@pytest.mark.django_db
def test_car_list_view(client):
    # Ro'yxat ko'rsatuvchi view uchun test
    url = reverse('car_list_cbv')
    response = client.get(url)

    # status_code 200 ekanini tekshirish
    assert response.status_code == 200
```

2. **`pytest` buyrug'i bilan barcha testlarni ishga tushirish:**
   ```powershell
   cd d:\jdu_django\car_market
   pytest -v
   ```

**Natija:**
```text
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-9.1.1, pluggy-1.6.0
django: version: 5.0.14, settings: config.settings (from ini)
rootdir: D:\jdu_django\car_market
configfile: pytest.ini
plugins: anyio-4.12.1, django-4.14.0
collected 4 items

carmarket/test_models.py::test_car_model PASSED                          [ 25%]
carmarket/test_views.py::test_car_list_view PASSED                       [ 50%]
carmarket/tests.py::CarAPITestCase::test_car_detail_api PASSED           [ 75%]
carmarket/tests.py::CarAPITestCase::test_car_list_api PASSED             [100%]

============================== 4 passed in 0.65s ==============================
```
Barcha testlar 100% muvaffaqiyatli (**PASSED**) yakunlandi!
