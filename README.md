# PlatForm-Django
Blog PlatForm-Django
# 📝 Blog Platform (پلتفرم وبلاگ با Django)

یک پروژه‌ی وبلاگ مدرن ساخته‌شده با **Django**، با طراحی شیشه‌ای (Glassmorphism) و ظاهر نئونی ✨
کاربران می‌تونن ثبت‌نام کنن، پست بزارن، و پروفایل خودشون رو ویرایش کنن.

---

## 🚀 ویژگی‌ها

* ثبت‌نام و ورود کاربران
* ساخت، ویرایش و حذف پست‌ها
* افزودن تصویر به پست‌ها
* دسته‌بندی (Category) و تگ‌ها
* سیستم کامنت‌گذاری
* صفحه‌ی پروفایل کاربر (با نام، بیو و عکس)
* نمایش پست‌های هر کاربر
* طراحی **واکنش‌گرا (Responsive)** برای موبایل
* استایل شیشه‌ای و درخشان با CSS سفارشی

---

## 🛠️ تکنولوژی‌های استفاده‌شده

* **Django 5+**
* **Python 3.11+**
* **Bootstrap 5**
* **HTML / CSS / JavaScript**
* **SQLite3** (پایگاه‌داده پیش‌فرض)
* فونت فارسی [Shabnam](https://fontcdn.ir/)

---

## 📂 ساختار پوشه‌ها (مهم‌ترین بخش‌ها)

```
📦 Blog-Platform-Django
├── blog/               # اپ اصلی وبلاگ
│   ├── models.py       # مدل‌های پست و کاربر
│   ├── views.py        # کنترلرها و منطق
│   ├── forms.py        # فرم‌های Django
│   ├── templates/      # قالب‌های HTML
│   └── static/css/     # فایل‌های CSS سفارشی
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## ⚙️ نحوه‌ی اجرا (روی سیستم خودت)

۱. ریپازیتوری رو کلون کن:

```bash
git clone https://github.com/Programmersogol/Blog-PlatForm-Django.git
cd Blog-PlatForm-Django
```

۲. محیط مجازی بساز:

```bash
python -m venv venv
source venv/Scripts/activate  # در ویندوز
```

۳. پکیج‌ها رو نصب کن:

```bash
pip install -r requirements.txt
```

۴. مایگریشن‌ها رو اجرا کن:

```bash
python manage.py migrate
```

۵. سرور رو بالا بیار:

```bash
python manage.py runserver
```

۶. سایت رو باز کن:

```
http://127.0.0.1:8000
```

---

## 👩‍💻 توسعه‌دهنده

**Programmersogol**
💡 عاشق طراحی وب، Django و پروژه‌های خلاقانه.

---

## 🌟 لایسنس

MIT License © 2025 — استفاده آزاد با ذکر منبع.
