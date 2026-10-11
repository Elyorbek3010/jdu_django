# 14-HAFTA UCHUN UY VAZIFASI: Kichik loyiha yaratish (Mini-project)
**Kurs:** Introduction to Django  
**O'qituvchi:** Erkaboy Qadamboyev  
**Talaba:** Elyorbek  
**Jurnal raqami:** 28 (28 - 20 = 8-variant: Avtomobil bozori — `carmarket` / Asosiy modellar: `Car`, `Brand`, `Listing`)  

---

## Nazariy qism (1–2-topshiriq)

### 1-topshiriq — Git branch nima uchun kerak?
**Javob:**
> **Git branch (tarmoq)** — bu asosiy kod bazasidan (masalan, `main` yoki `master` tarmog'idan) ajralib chiqqan holda, yangi funksionallik (feature) qo'shish yoki xatolarni tuzatish (bugfix) uchun alohida, xavfsiz va mustaqil ishchi maydon yaratish mexanizmidir.
> 
> U dasturchilarga asosiy ishlayotgan kodga ta'sir qilmasdan, mustaqil tajriba qilish va bir vaqtning o'zida jamoada bir nechta vazifani parallel bajarish imkoniyatini beradi. Yangi qism to'liq tayyor bo'lib, testlardan o'tgandan so'ng, u yana asosiy tarmoqqa xavfsiz birlashtiriladi (`git merge`).

---

### 2-topshiriq — `.gitignore` nima uchun kerak va u bo'lmasa nima xato yuz berishi mumkin?
**Javob:**
> **`.gitignore`** — bu Git versiya nazorati tizimiga repozitoriyga qo'shilishi shart bo'lmagan, vaqtinchalik yoki maxfiy fayl va papkalarni e'tiborsiz qoldirishni (ignore qilishni) buyuruvchi maxsus konfiguratsiya faylidir.
> 
> **U bo'lmasa qanday xatolar yuz beradi:**
> 1. **Maxfiy ma'lumotlar oshkor bo'lishi:** `.env` fayllari, maxfiy parollar, SECRET_KEY yoki API kalitlar GitHub ommaviy repozitoriyasiga chiqib ketib, xavfsizlikka jiddiy xavf tug'diradi.
> 2. **Loyiha bazasining buzilishi va konfliktlar:** `db.sqlite3` bazasi yoki virtual muhit (`venv/`) qo'shilib ketsa, repozitoriy hajmi yuzlab megabaytga oshadi va jamoa a'zolari o'rtasida ziddiyatlar (merge conflict) yuzaga keladi.
> 3. **Keraksiz keshlar:** `__pycache__/`, `.pytest_cache/` kabi operatsion tizim yoki kompilyator kesh fayllari repozitoriy tarixini ifloslantiradi.

---

## Amaliy qism (3–5-topshiriq)

### Talaba varianti ma'lumotlari:
- **Jurnal raqami:** 28
- **Variant:** `28 - 20 = 8`
- **Loyiha nomi:** Avtomobil bozori (`carmarket`)
- **Asosiy modellar:** `Car`, `Brand`, `Listing` (qo'shimcha: `Category`)

---

### 3-topshiriq — Loyihani rejalashtirish va Git bilan boshlash

#### 1. Loyiha rejasi (Arxitektura):
* **Modellar arxitekturasi:**
  - `Brand`: Avtomobil ishlab chiqaruvchi brend ma'lumotlari (`name`, `country`).
  - `Category`: Avtomobil toifasi (`name` — masalan: Sedan, SUV, Hechbek).
  - `Car`: Sotuvga qo'yiladigan avtomobil asosiy texnik xususiyatlari (`brand`, `brand_ref`, `model`, `price`, `year`, `image`, `category`).
  - `Listing`: Foydalanuvchilar tomonidan joylashtiriladigan e'lon (`car`, `author`, `title`, `description`, `created_at`, `is_active`).

* **Asosiy sahifalar (URL yo'nalishlari):**
  - `/cars/fbv/` va `/cars/cbv/` — Avtomobillar ro'yxati (List View).
  - `/cars/<id>` — Tanlangan avtomobilning batafsil sahifasi (Detail View).
  - `/cars/add/` — Yangi avtomobil kiritish formasi (Create View — himoyalangan).
  - `/register/` — Yangi foydalanuvchini ro'yxatdan o'tkazish.
  - `/login/` va `/logout/` — Tizimga kirish va chiqish.
  - `/api/carmarket/` — REST API endpointlari.

* **Foydalanuvchi rollari:**
  - **Anonim mehmon (Guest):** Mashinalar ro'yxatini va batafsil sahifasini ko'ra oladi, ro'yxatdan o'tishi mumkin.
  - **Tizim foydalanuvchisi (Authenticated User):** Tizimga kirib, yangi avtomobil e'lonlarini joylay oladi (`@login_required` bilan himoyalangan).
  - **Superuser (Admin):** Django ma'muriy paneli orqali barcha brendlar, mashinalar, e'lonlar va foydalanuvchilarni to'liq boshqaradi.

#### 2. Git bilan boshlash amallari:
1. Loyiha ildizida `.gitignore` yaratildi (`db.sqlite3`, `__pycache__/`, `.pytest_cache/`, `media/`, `venv/`).
2. Repozitoriy ishga tushirildi:
   ```powershell
   git init
   git add .
   git commit -m "feat: 14-hafta kichik loyiha - Avtomobil bozori (carmarket)"
   ```
3. GitHub repozitoriyasiga ulash va push qilish:
   ```powershell
   git branch -M main
   git remote add origin https://github.com/<GITHUB_USERNAME>/<REPO_NAME>.git
   git push -u origin main
   ```

---

### 4-topshiriq — Asosiy funksionallikni birlashtirish

1. **Modellar (`carmarket/models.py`):**
   `Brand`, `Car`, `Listing` va `Category` modellari o'zaro `ForeignKey` munosabatlari bilan bog'langan.
2. **Ro'yxat va Detail View'lari (`carmarket/views.py`):**
   - Ro'yxat: `car_list_fbv` va `CarListView` (Class-based).
   - Batafsil ma'lumot: `get_car_detail(request, id)`.
3. **Formalar va yaratish (`carmarket/forms.py`):**
   - `CarForm` (ModelForm) orqali ma'lumotlar va rasm yuklash shakli.
   - `car_create(request)` view orqali yangi avtomobillar bazaga saqlanadi.
4. **Shablonlar (Templates):**
   - `carmarket/templates/carmarket/car_list.html`
   - `carmarket/templates/carmarket/car_detail.html`
   - `carmarket/templates/carmarket/car_form.html`

---

### 5-topshiriq — Autentifikatsiya qo'shish

1. **Ro'yxatdan o'tish (`carmarket/views.py`):**
   - `register(request)` view'si `UserCreationForm` yordamida yangi foydalanuvchini yaratadi va tizimga avtomatik kiritadi (`login(request, user)`).
2. **Kirish va Chiqish (`carmarket/urls.py`):**
   - `path('login/', LoginView.as_view(...))`
   - `path('logout/', LogoutView.as_view(...))`
3. **Sahifalarni `@login_required` bilan himoyalash:**
   - Mashinalar ro'yxati (`car_list_fbv`) va yangi mashina qo'shish (`car_create`) sahifalari `@login_required` dekoratori bilan himoyalangan. Tizimga kirmagan foydalanuvchilar avtomatik tarzda `/login/` sahifasiga yo'naltiriladi.

---

## 🧪 Loyihani sinovdan o'tkazish

1. **Pytest orqali barcha testlarni yurgizish:**
   ```powershell
   cd d:\jdu_django\car_market
   pytest -v
   ```
   **Natija:** 4 ta test muvaffaqiyatli o'tdi (**PASSED**).

2. **Loyiha serverini ishga tushirish:**
   ```powershell
   python manage.py runserver
   ```
   - Asosiy ro'yxat: `http://127.0.0.1:8000/cars/fbv/`
   - Kirish sahifasi: `http://127.0.0.1:8000/login/`
   - Yangi mashina qo'shish: `http://127.0.0.1:8000/cars/add/`
