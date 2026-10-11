# 2-HAFTA UCHUN UY VAZIFASI: Django loyiha strukturasi
**Kurs:** Introduction to Django  
**O'qituvchi:** Erkaboy Qadamboyev  
**Talaba:** Elyorbek  
**Jurnal raqami:** 28 (28 - 20 = 8-variant: Avtomobil bozori — `carmarket`)  

---

## Nazariy qism

### 1-topshiriq — Loyiha fayllari
Django loyihasi va ilovasida joylashgan asosiy fayllar va ularning vazifalari:

1. **`manage.py`**:
   - Loyihani boshqarish uchun mo'ljallangan asosiy CLI (Command Line Interface) vositasi.
   - U orqali serverni ishga tushirish (`python manage.py runserver`), yangi app yaratish (`startapp`), ma'lumotlar bazasi migratsiyalarini bajarish (`makemigrations`, `migrate`), superuser yaratish (`createsuperuser`) va loyihani tekshirish (`check`) amalga oshiriladi.

2. **`settings.py`**:
   - Loyihaning markaziy konfiguratsiya fayli.
   - Barcha muhim sozlamalar shu yerda joylashadi: ulangan ilovalar ro'yxati (`INSTALLED_APPS`), ma'lumotlar bazasi ulanishi (`DATABASES`), xavfsizlik kaliti (`SECRET_KEY`), dasturni sozlash rejimi (`DEBUG`), til va vaqt mintaqasi (`LANGUAGE_CODE`, `TIME_ZONE`), statik fayllar yo'li (`STATIC_URL`).

3. **`urls.py`**:
   - Loyihaning marshrutlash (routing) xaritasi.
   - Foydalanuvchi brauzer orqali murojaat qilgan URL manzillarini tegishli ko'rinishlar (view) yoki ilovalarga yo'naltiruvchi `urlpatterns` ro'yxatini o'z ichiga oladi.

4. **`wsgi.py` (Web Server Gateway Interface)**:
   - Loyihani serverlarga (masalan, Gunicorn, uWSGI, Nginx, Apache) sinxron tarzda ishlab chiqarish (production) muhitiga joylashtirish uchun kirish nuqtasi.

5. **`asgi.py` (Asynchronous Server Gateway Interface)**:
   - Asinxron imkoniyatlar (WebSockets, chatlar, real vaqt xabarlari, async views) bilan ishlash uchun zamonaviy asinxron kirish nuqtasi (Daphne, Uvicorn serverlari orqali ishlatiladi).

6. **`__init__.py`**:
   - Python dasturiga ushbu papkani oddiy papka emas, balki import qilib bo'ladigan Python paketi (package) sifatida tanituvchi fayl.

#### Ilova (App) ichidagi asosiy fayllar:
- **`models.py`** — Ma'lumotlar bazasining tuzilishi (jadvallar va ustunlar) Python klasslari (ORM) shaklida belgilanadi.
- **`views.py`** — Foydalanuvchining so'rovlarini qabul qilib, kerakli ma'lumotlarni qayta ishlovchi va javob (HTML sahifa yoki JSON) qaytaruvchi funksiya yoki klasslar yoziladi.
- **`admin.py`** — Loyihadagi modellarni Django'ning tayyor Admin boshqaruv panelida ko'rsatish va sozlash joyi.
- **`apps.py`** — Shu ilovaning o'ziga xos sozlamalari (Application Configuration).
- **`tests.py`** — Kodning sifatini va to'g'ri ishlashini tekshirish uchun testlar yozish fayli.
- **`migrations/`** — Modellarga kiritilgan o'zgarishlarni ma'lumotlar bazasiga xavfsiz o'tkazish tarixi saqlanadigan papka.

---

### 2-topshiriq — Project va App farqi

**Javob:**
- **Project (Loyiha)** — Bu butun bir mustaqil veb-sayt yoki veb-tizim. U umumiy konfiguratsiya (`settings.py`), asosiy marshrutlar (`urls.py`) va ma'lumotlar bazasi parametrlarini birlashtirib turadi. Loyiha o'z ichida bir yoki bir nechta ilovalarni (app) jamlaydi.
- **App (Ilova)** — Bu loyiha ichida faqat aniq, bitta maqsadli funksionallikni bajaruvchi mustaqil modul. Masalan:
  - `carmarket` — avtomobillar e'loni va qidiruv tizimi;
  - `users` — ro'yxatdan o'tish va profil boshqaruvi;
  - `payments` — to'lovlarni qabul qilish.

> **Oddiy o'xshatish:**  
> **Project** — bu butun bir smartfon (telefon apparati va uning umumiy sozlamalari).  
> **App** — bu telefonga o'rnatilgan har bir alohida dastur (Telegram, Kamera, Galereya). Har bir ilova o'z vazifasini bajaradi, kerak bo'lsa boshqa loyihalarda ham qayta ishlatilishi (reusable app) mumkin.

---

## Amaliy qism

### Talaba va variant ma'lumotlari:
- **Jurnal raqami:** 28
- **Variant hisobi:** 21-talabadan boshlab qayta 1-variantdan boshlanadi: `28 - 20 = 8`
- **8-variant mavzusi:** Avtomobil bozori
- **Ilova nomi (startapp):** `carmarket`

---

### 3-topshiriq — Loyiha fayllarini o'rganish

1. **`config/settings.py` faylida ko'rsatiladigan asosiy parametrlar:**
   - **`INSTALLED_APPS` (33-qator):** Loyihada ulangan va faol bo'lgan barcha ilovalar ro'yxati (Django'ning tayyor tizim ilovalari hamda biz yaratgan shaxsiy ilovalar).
   - **`DATABASES` (78-qator):** Loyiha ishlatayotgan ma'lumotlar bazasi sozlamalari (standart holatda `sqlite3` drayveri va `db.sqlite3` fayli ko'rsatilgan).
   - **`TIME_ZONE` (110-qator):** Loyiha vaqt zonalari bo'yicha qaysi vaqt bilan ishlashini belgilaydi (standart holatda `UTC`).
   - **`LANGUAGE_CODE` (108-qator):** Tizim tili (`uz` deb belgilangan).

2. **`config/urls.py` faylida ko'rsatiladigan asosiy parametr:**
   - **`urlpatterns` (20-qator):** Loyihaning asosiy URL yo'llari ro'yxati (standart holatda admin panel uchun `path('admin/', admin.site.urls)` mavjud).

---

### 4-topshiriq — Yangi ilova (app) yaratish

Loyiha papkasida terminal orqali quyidagi buyruq bajarildi:
```powershell
cd d:\jdu_django\car_market
python manage.py startapp carmarket
```

**Natija:**
`car_market` papkasida `carmarket` nomli yangi Django ilovasi va uning ichki fayllari (`admin.py`, `apps.py`, `models.py`, `views.py`, `tests.py`, `migrations/`) muvaffaqiyatli yaratildi.

---

### 5-topshiriq — Ilovani loyihaga ulash

`car_market/config/settings.py` faylidagi `INSTALLED_APPS` ro'yxatiga `'carmarket'` qo'shildi:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Loyiha ilovalari (Custom apps)
    'carmarket',
]
```

Tizim tekshirildi:
```powershell
python manage.py check
```
Natija: `System check identified no issues (0 silenced).`

---

## Darsda o'qituvchiga ko'rsatish tartibi va og'zaki javoblar rejasi:

1. **Terminalda loyihani ishga tushirish:**
   ```powershell
   cd d:\jdu_django\car_market
   python manage.py check
   python manage.py runserver
   ```
2. **VS Code muharririda ekranda ko'rsatish:**
   - Chap tomondagi fayllar daraxtida yangi ochilgan **`carmarket`** papkasini va uning ichidagi fayllarni ko'rsatish.
   - **`config/settings.py`** faylini ochib:
     - `INSTALLED_APPS` ro'yxatida oxirgi qo'shilgan `'carmarket'` qatorini ko'rsatish (3-topshiriq & 5-topshiriq).
     - `DATABASES` blokini ko'rsatib: *"Bu yerda loyihamiz qaysi ma'lumotlar bazasiga ulanishi ko'rsatilgan, hozirda SQLite3 ishlatilmoqda"* deb aytish.
     - `TIME_ZONE` va `LANGUAGE_CODE` qatorlarini ko'rsatish.
   - **`config/urls.py`** faylini ochib:
     - `urlpatterns` ro'yxatini ko'rsatib: *"Bu loyihaning barcha sahifalari va URL yo'llari ro'yxatga olinadigan asosiy marshrutlar xaritasi"* deb aytish.
3. **Og'zaki savol-javobga tayyorgarlik:**
   - *Loyiha fayllari haqida so'ralsa:* `manage.py` — buyruqlar markazi, `settings.py` — loyiha sozlamalari, `urls.py` — sahifalar marshruti ekanligini aytish.
   - *Project va App farqi so'ralsa:* *"Project — butun veb-sayt va uning umumiy konfiguratsiyasi. App esa shu sayt ichidagi bitta mustaqil modul (masalan, bizdagi `carmarket` avtomobil bozori moduli)"* deb tushuntirish.
