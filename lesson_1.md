# 1-HAFTA UCHUN UY VAZIFASI: Django bilan tanishuv
**Kurs:** Introduction to Django  
**O'qituvchi:** Erkaboy Qadamboyev  
**Talaba:** Elyorbek  

---

## Nazariy qism

### 1-topshiriq — Veb-freymvork nima?
**Javob:**
> **Veb-freymvork (Web framework)** — bu veb-saytlar va veb-ilovalarni tez, xavfsiz hamda qulay yaratish uchun mo'ljallangan tayyor dasturiy qolip, qoidalar va kutubxonalar to'plamidir.
> 
> Dasturchi har bir loyihada noldan boshlab HTTP so'rovlarini qabul qilish, marshrutlash (routing), ma'lumotlar bazasi bilan ulanish, xavfsizlik va shablonlar (HTML) render qilish kabi takroriy ishlarni qo'lda yozib o'tirmaydi. Freymvork ushbu umumiy vazifalarni o'z zimmasiga oladi va dasturchiga faqat loyihaning o'ziga xos biznes mantiqini (logic) yozishga diqqat qaratish imkonini beradi.

---

### 2-topshiriq — Django xususiyatlari
**Javob (Django’ning asosiy xususiyatlari):**
1. **"Batteries-included" (Barcha kerakli vositalar ichida):**
   Django loyiha yaratish uchun kerak bo'ladigan deyarli barcha narsani tayyor holda taqdim etadi — tayyor Admin panel, qulay ORM (ma'lumotlar bazasi bilan ishlash), foydalanuvchilar autentifikatsiyasi va sessiyalarni boshqarish tizimi mavjud. Qo'shimcha uchinchi tomon paketlariga kamroq ehtiyoj seziladi.

2. **Keng qamrovli xavfsizlik (Built-in Security):**
   Django xavfsizlikni birinchi o'ringa qo'yadi. U SQL Injection, CSRF (Cross-Site Request Forgery), XSS (Cross-Site Scripting) va Clickjacking kabi eng keng tarqalgan veb-zaifliklardan avtomatik va ishonchli himoyalaydi.

3. **MVT (Model-View-Template) arxitekturasi:**
   Loyiha mantiqini aniq qatlamlarga ajratadi:
   - **Model:** Ma'lumotlar tuzilishi va baza bilan ishlash.
   - **View:** Biznes mantiq va so'rovlarni boshqarish.
   - **Template:** Foydalanuvchiga ko'rinadigan foydalanuvchi interfeysi (UI/HTML).  
   Bu esa kodni toza, o'qilishi oson va loyihani kelajakda kengaytirish (scalability) uchun juda qulay qiladi.

---

## Amaliy qism

### 3-topshiriq — Python va Django o'rnatish
- **Python holati:** O'rnatilgan (Python 3.12.7)
- **Django holati:** O'rnatilgan (Django 5.0.14)

### 4-topshiriq — Shaxsiy loyiha yaratish
- **Jurnal raqami:** 28
- **Loyiha mavzusi:** Avtomobil bozori (Car Market)
- **Loyiha nomi:** `car_market`
- **Yaratish buyrug'i:**
  ```powershell
  django-admin startproject car_market
  ```
- **Loyiha papkasiga o'tish:**
  ```powershell
  cd car_market
  ```
- **Loyihani ishga tushirish (runserver):**
  ```powershell
  python manage.py runserver
  ```
- **Natija:** Brauzerda `http://127.0.0.1:8000/` manzilini ochganda Django tabrik sahifasi (The install worked successfully!) ochiladi.

---

### 5-topshiriq — Kichik o'zgartirish kiritish
- `car_market/car_market/settings.py` faylida quyidagi qator o'zgartirildi:
  ```python
  # Oldingi holati:
  # LANGUAGE_CODE = 'en-us'

  # Yangi holati (o'zbek tili uchun):
  LANGUAGE_CODE = 'uz'
  ```
- O'zgarish saqlandi va tizim tekshirildi (`python manage.py check` muvaffaqiyatli o'tdi).

---

## Darsda o'qituvchiga ko'rsatish tartibi:
1. Terminal / PowerShell ochish.
2. Loyiha papkasiga kirish:
   ```powershell
   cd d:\jdu_django\car_market
   ```
3. Serverni ishga tushirish:
   ```powershell
   python manage.py runserver
   ```
4. Brauzerda [http://127.0.0.1:8000/](http://127.0.0.1:8000/) havolasini ochib ko'rsatish.
5. VS Code yoki boshqa muharrirda `car_market/car_market/settings.py` faylidagi `LANGUAGE_CODE = 'uz'` qatorini ko'rsatish.
