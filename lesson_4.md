# 4-HAFTA UCHUN UY VAZIFASI: Django Views va Templates
**Kurs:** Introduction to Django  
**O'qituvchi:** Erkaboy Qadamboyev  
**Talaba:** Elyorbek  
**Jurnal raqami:** 28 (28 - 20 = 8-variant: Avtomobil bozori — `carmarket` / Model: `Car`)  

---

## Nazariy qism (1–2-topshiriq)

### 1-topshiriq — View va Template
* **View (Ko'rinish):** Foydalanuvchining brauzerdan yuborgan HTTP so'rovini (request) qabul qiluvchi, ma'lumotlar bazasidan (Model orqali) kerakli ma'lumotlarni oluvchi va biznes-mantiqni boshqaruvchi markazdir. U tayyorlangan ma'lumotlarni Template'ga uzatadi va foydalanuvchiga yakuniy HTTP javobni (response) qaytaradi.
* **Template (Shablon):** Foydalanuvchiga ko'rinadigan grafik interfeys (HTML fayl) hisoblanadi. U View tomonidan yuborilgan dinamik ma'lumotlarni Django Template Language (DTL — `{{ }}`, `{% %}`) yordamida chiroyli, tushunarli va qulay ko'rinishda sahifaga chiqarib berish uchun kerak.

---

### 2-topshiriq — FBV va CBV farqi
* **Function-Based View (FBV):** Oddiy Python funksiyasi ko'rinishida yoziladi. So'rov turlari (GET, POST) funksiya ichida `if request.method == 'POST'` shartlari orqali tekshiriladi. Uning afzalligi — mantiq juda oddiy, tushunish va o'qish oson bo'lib, kichik va nostandart vazifalar uchun qulay.
* **Class-Based View (CBV):** Python klassi shaklida yoziladi va Django'ning tayyor generik klasslaridan (masalan, `ListView`, `DetailView`, `CreateView`) meros oladi. Uning afzalligi — kod hajmini sezilarli darajada qisqartiradi (DRY prinsipi), takroriy ishlarni avtomatlashtiradi hamda obyektga yo'naltirilgan dasturlash (OOP) imkoniyatlaridan (meros olish va metodlarni qayta yozish) foydalanish imkonini beradi.

---

## Amaliy qism (Mustaqil bajarish uchun qo'llanma)

### 3-topshiriq — Function-based view yaratish
1. `carmarket/views.py` faylini oching.
2. `Car` modelini import qiling:
   ```python
   from .models import Car
   ```
3. `car_list_fbv(request)` nomli funksiya yozing:
   - Bazadagi barcha mashinalarni olish: `cars = Car.objects.all()`
   - Ma'lumotlarni lug'at (dict) ichiga joylash: `context = {'cars': cars}`
   - `render(request, 'carmarket/car_list.html', context)` bilan qaytarish.

---

### 4-topshiriq — Template yaratish
1. `carmarket/` papkasi ichida `templates/carmarket/` papkalarini oching:
   - Yo'l: `carmarket/templates/carmarket/car_list.html`
2. HTML fayl yaratib, ichida `{% for car in cars %}` siklidan foydalaning:
   ```html
   {% for car in cars %}
       <div style="border: 1px solid #ccc; margin: 10px; padding: 10px;">
           <h2>{{ car.brand }} {{ car.model }}</h2>
           <p>Narxi: ${{ car.price }}</p>
           <p>Yili: {{ car.year }}</p>
       </div>
   {% empty %}
       <p>Hozircha mashinalar kiritilmagan.</p>
   {% endfor %}
   ```

---

### 5-topshiriq — Class-based view bilan qayta yozish
1. `carmarket/views.py` fayliga `ListView`ni import qiling:
   ```python
   from django.views.generic import ListView
   ```
2. `CarListView` nomli klass yozing:
   ```python
   class CarListView(ListView):
       model = Car
       template_name = 'carmarket/car_list.html'
       context_object_name = 'cars'
   ```
3. Ikkala ko'rinishni ham ishlatish uchun `carmarket/urls.py` faylini yaratib, yo'llarni bog'lang:
   - FBV uchun: `path('cars/fbv/', car_list_fbv, name='car_list_fbv')`
   - CBV uchun: `path('cars/cbv/', CarListView.as_view(), name='car_list_cbv')`
4. `config/urls.py` fayliga `include('carmarket.urls')` ni qo'shing.

---

## Darsda o'qituvchiga ko'rsatish tartibi:
1. Serverni ishga tushirish:
   ```powershell
   cd d:\jdu_django\car_market
   python manage.py runserver
   ```
2. Brauzerda ikkala manzilni ko'rsatish:
   - FBV: `http://127.0.0.1:8000/cars/fbv/`
   - CBV: `http://127.0.0.1:8000/cars/cbv/`
3. Muharrirda `views.py` va `car_list.html` dagi kodlarni ko'rsatish.
