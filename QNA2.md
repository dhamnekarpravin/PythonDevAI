# Day 5: Django Project Setup - Interview Questions

## 1. What is a Django project?
A Django project is a collection of settings and apps for a particular website. It's the top-level directory that contains configuration files and multiple apps.

```bash
django-admin startproject myproject
```

**Simple answer:** A project is the main container for your website, holding all the configuration and apps.

---

## 2. What is a Django app?
An app is a self-contained module that does a specific function. A project can have multiple apps (e.g., users, tasks, blog).

```bash
python manage.py startapp tasks
```

**Simple answer:** An app is a building block that handles one specific feature of your website.

---

## 3. What is the difference between a project and an app?
- **Project**: The entire website configuration, contains multiple apps
- **App**: A specific feature module, can be reused in different projects

**Simple answer:** Project is the whole website; app is one feature within it.

---

## 4. What is settings.py?
`settings.py` is the main configuration file for a Django project. It contains database settings, installed apps, middleware, static files, and security settings.

```python
DEBUG = True
INSTALLED_APPS = ['tasks', 'users']
DATABASES = {...}
```

**Simple answer:** The control panel where you configure everything about your Django project.

---

## 5. What is urls.py?
`urls.py` maps URLs to views. It tells Django which view function to call when a user visits a specific URL.

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

**Simple answer:** The traffic controller that directs URLs to the right view functions.

---

## 6. What is a view?
A view is a Python function that takes a web request and returns a web response. It contains the logic for your page.

```python
def home(request):
    return render(request, 'home.html')
```

**Simple answer:** A function that processes requests and sends back HTML or data.

---

## 7. What is a template?
A template is an HTML file with placeholders for dynamic data. Django fills in the placeholders with actual data before sending to the browser.

```html
<h1>{{ app_name }}</h1>
<p>{{ message }}</p>
```

**Simple answer:** An HTML file with special tags for inserting dynamic content.

---

## 8. What are static files?
Static files are assets that don't change - CSS, JavaScript, images, and fonts. They're served separately from dynamic content.

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

**Simple answer:** Files like CSS, images, and JS that stay the same for every user.

---

## 9. How do you run the Django development server?
Use the `runserver` command to start the development server for testing.

```bash
python manage.py runserver
```

**Simple answer:** The command to start Django's built-in server for development.

---

## 10. What is the purpose of manage.py?
`manage.py` is a command-line utility for Django project tasks - running the server, creating migrations, creating apps, and more.

```bash
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
```

**Simple answer:** A tool that lets you run common Django commands from the terminal.

---

# Project-Based Questions

## 11. Why did you separate your project into apps?
Separating into apps makes code organized, reusable, and easier to maintain. Each app handles one feature independently.

**Simple answer:** Keeps code organized by feature, making it easier to work on and reuse.

---

## 12. How does Django find templates?
Django looks for templates in the `templates` folder of each app and in the `TEMPLATES` DIRS setting in `settings.py`.

```python
TEMPLATES = [
    {
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
    }
]
```

**Simple answer:** Django checks the templates folder in your project and in each app.

---

## 13. What does `{% load static %}` do?
It loads the static template tag library, allowing you to use `{% static %}` to reference static files in your templates.

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

**Simple answer:** Enables the use of static file references in your HTML templates.

---

## 14. Why use `DEBUG = True` in development?
`DEBUG = True` shows detailed error pages with stack traces when something goes wrong, making it easier to debug issues during development.

**Simple answer:** Shows helpful error messages to help you fix problems while building.

---

## 15. How do you add a new app to Django?
1. Create the app: `python manage.py startapp appname`
2. Add it to `INSTALLED_APPS` in `settings.py`
3. Create URLs, views, and templates

**Simple answer:** Create the app, register it in settings, then build your URLs and views.
