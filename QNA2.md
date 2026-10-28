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

---

# Day 6: Django Models and Admin - Interview Questions

## 16. What is a Django model?
A Django model is a Python class that represents a database table. Each model field maps to a database column.

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
```

**Simple answer:** A Python class that automatically becomes a database table.

---

## 17. What are common Django model fields?
- **CharField**: Short text (strings)
- **TextField**: Long text
- **IntegerField**: Whole numbers
- **BooleanField**: True/False
- **DateField**: Date
- **DateTimeField**: Date and time
- **ForeignKey**: Relationship to another model
- **ManyToManyField**: Many-to-many relationship

**Simple answer:** Different field types for storing different kinds of data in the database.

---

## 18. What are Django migrations?
Migrations are Django's way of propagating changes to your models into the database schema.

```bash
python manage.py makemigrations  # Create migration file
python manage.py migrate         # Apply migration to database
```

**Simple answer:** Files that track and apply changes to your database structure.

---

## 19. What is a QuerySet?
A QuerySet is a list of objects from a database. It lets you filter, order, and manipulate data.

```python
# Get all tasks
tasks = Task.objects.all()

# Filter tasks
completed_tasks = Task.objects.filter(completed=True)

# Get single task
task = Task.objects.get(id=1)
```

**Simple answer:** A tool to query and filter data from the database.

---

## 20. What is a ForeignKey?
A ForeignKey creates a many-to-one relationship between two models. It links one model to another.

```python
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
```

**Simple answer:** A link that connects one item to another (like a task belonging to a project).

---

## 21. What does `on_delete` do in ForeignKey?
`on_delete` specifies what happens when the referenced object is deleted.

- **CASCADE**: Delete the related object too
- **SET_NULL**: Set the field to NULL
- **PROTECT**: Prevent deletion
- **SET_DEFAULT**: Set to default value

**Simple answer:** Tells Django what to do with related items when the parent is deleted.

---

## 22. What is the Django admin?
The Django admin is a built-in interface for managing your site's data. It automatically creates forms for your models。

```python
from django.contrib import admin
admin.site.register(Task)
```

**Simple answer:** A ready-made dashboard to manage your database without writing code.

---

## 23. How do you customize the Django admin?
Create an admin class and register it with your model to customize display, filters, and search.

```python
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "priority")
    list_filter = ("status", "priority")
    search_fields = ("title", "description")
```

**Simple answer:** Add an admin class to control how your data appears and can be managed.

---

## 24. What are environment variables?
Environment variables are configuration values stored outside your code, like API keys or database passwords. They keep sensitive data secure.

```python
import environ
env = environ.Env()
SECRET_KEY = env("SECRET_KEY")
```

**Simple answer:** Settings stored outside your code to keep secrets safe and make deployment easier.

---

## 25. What is django-environ?
`django-environ` is a library that helps you read environment variables from a `.env` file and use them in Django settings.

```python
import environ
env = environ.Env()
environ.Env.read_env()
DEBUG = env("DEBUG", default=False)
```

**Simple answer:** A tool to load configuration from a `.env` file instead of hardcoding it.

---

## 26. What is the difference between `auto_now_add` and `auto_now`?
- **auto_now_add**: Sets the field to now when the object is first created
- **auto_now**: Updates the field to now every time the object is saved

```python
created_at = models.DateTimeField(auto_now_add=True)  # Set once
updated_at = models.DateTimeField(auto_now=True)     # Update every save
```

**Simple answer:** auto_now_add for creation time; auto_now for last update time.

---

## 27. What are model choices?
Choices restrict a field to specific values, useful for dropdowns and status fields.

```python
STATUS_CHOICES = [
    ("pending", "Pending"),
    ("completed", "Completed"),
]
status = models.CharField(max_length=20, choices=STATUS_CHOICES)
```

**Simple answer:** A list of allowed values for a field, like a dropdown menu.

---

## 28. What is the `__str__` method in models?
`__str__` defines how a model object displays as a string, useful in admin and debugging.

```python
def __str__(self):
    return self.title
```

**Simple answer:** Controls what text shows when you print or display the object.

---

## 29. What is a model property?
A property is a computed field that doesn't exist in the database but can be accessed like one.

```python
@property
def is_overdue(self):
    return self.due_date < timezone.now()
```

**Simple answer:** A dynamic field calculated from other data, not stored in the database.

---

## 30. What is the Meta class in models?
The Meta class contains model-level options like ordering, table names, and permissions.

```python
class Meta:
    ordering = ["-created_at"]
    verbose_name = "Task"
    indexes = [models.Index(fields=["status"])]
```

**Simple answer:** Settings that control how the model behaves and is organized.

---

# Project-Based Questions

## 31. Why did you use ForeignKey in your models?
ForeignKey creates relationships between models, like tasks belonging to projects. This organizes data and enables queries like "get all tasks for project X".

**Simple answer:** Links related data together so you can organize and query it efficiently.

---

## 32. How do you handle environment variables in Django?
Use `django-environ` to read from a `.env` file, keeping sensitive data like SECRET_KEY out of your code. Add `.env` to `.gitignore` to avoid committing secrets.

**Simple answer:** Store secrets in a `.env` file and load them with django-environ.

---

## 33. Why customize the Django admin?
Customizing the admin improves usability by showing relevant fields, adding filters, and enabling search. This makes managing data faster and easier.

**Simple answer:** Makes the admin interface more user-friendly and efficient for your specific data.

---

## 34. What is the purpose of migrations?
Migrations track database changes over time, allowing you to version control your schema and roll back if needed. They ensure team members have the same database structure.

**Simple answer:** Track and apply database changes in a controlled, versioned way.

---

## 35. How do you add a new field to an existing model?
1. Add the field to the model class
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`

**Simple answer:** Add the field to the model, then create and apply the migration.
