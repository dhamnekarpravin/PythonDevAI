# Day 7: Django Templates and Forms - Interview Questions

## 1. What is template inheritance?
Template inheritance lets you create a base template with common layout and extend it in child templates. This avoids repeating HTML structure.

```html
<!-- base.html -->
<html>
<body>
    {% block content %}{% endblock %}
</body>
</html>

<!-- child.html -->
{% extends "base.html" %}
{% block content %}
    <h1>My content here</h1>
{% endblock %}
```

**Simple answer:** Create a parent template with common layout, then child templates fill in the specific parts.

---

## 2. What is template context?
Context is a dictionary that passes data from views to templates. Views send data, templates display it.

```python
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})
```

```html
{% for task in tasks %}
    <p>{{ task.title }}</p>
{% endfor %}
```

**Simple answer:** Data sent from your view to the template for display.

---

## 3. What are Django template tags?
Template tags are special syntax that performs logic in templates, like loops, conditions, and loading libraries.

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}</p>
{% endif %}

{% for task in tasks %}
    <p>{{ task.title }}</p>
{% endfor %}

{% load static %}
```

**Simple answer:** Special commands inside {% %} that do things in templates.

---

## 4. What are Django template filters?
Filters modify variables before displaying them, like formatting dates, capitalizing text, or truncating.

```html
{{ task.title|upper }}           <!-- UPPERCASE -->
{{ task.created_at|date:"Y-m-d" }} <!-- Format date -->
{{ description|truncatewords:10 }}  <!-- Truncate text -->
```

**Simple answer:** Tools to change how data looks when displayed.

---

## 5. What is a Django form?
A Django form is a class that handles form rendering, validation, and data processing. It maps to HTML form elements.

```python
from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.TextField()
```

**Simple answer:** A Python class that creates and validates HTML forms.

---

## 6. What is a ModelForm?
A ModelForm automatically generates a form based on a Django model, saving you from defining fields manually.

```python
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
```

**Simple answer:** A form that automatically matches your model fields.

---

## 7. How do you validate a form?
Call `is_valid()` on the form to check if data is valid. Access errors with `form.errors`.

```python
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})
```

**Simple answer:** Call is_valid() to check, then save if valid or show errors if not.

---

## 8. How do you display form errors in a template?
Use `form.errors` to show validation errors, or loop through field-specific errors.

```html
{% if form.errors %}
    <div class="error">
        {% for field in form %}
            {% if field.errors %}
                <p>{{ field.label }}: {{ field.errors }}</p>
            {% endif %}
        {% endfor %}
    </div>
{% endif %}
```

**Simple answer:** Check form.errors and display them to help users fix mistakes.

---

## 9. What are Django messages?
Django messages framework lets you store temporary messages (success, error, info) to display after a redirect.

```python
from django.contrib import messages

def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Task created successfully!')
        return redirect('task_list')
```

```html
{% if messages %}
    {% for message in messages %}
        <div class="alert">{{ message }}</div>
    {% endfor %}
{% endif %}
```

**Simple answer:** A way to show notifications like "Task saved" after an action.

---

## 10. What is pagination?
Pagination splits large lists of data into multiple pages, improving performance and user experience.

```python
from django.core.paginator import Paginator

def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tasks/list.html', {'page_obj': page_obj})
```

```html
{% for task in page_obj %}
    <p>{{ task.title }}</p>
{% endfor %}

<div class="pagination">
    {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
    {% endif %}
    <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
</div>
```

**Simple answer:** Breaking long lists into separate pages instead of showing everything at once.

---

## 11. What is the difference between `{{ variable }}` and `{% tag %}`?
- `{{ variable }}`: Outputs the value of a variable
- `{% tag %}`: Executes logic like if, for, or load

```html
{{ task.title }}        <!-- Display value -->
{% if task.completed %} <!-- Execute logic -->
    <p>Done!</p>
{% endif %}
```

**Simple answer:** Double braces display data; percent signs do logic.

---

## 12. What is CSRF protection?
CSRF (Cross-Site Request Forgery) protection prevents malicious websites from submitting forms on your behalf. Django adds a CSRF token to forms.

```html
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

**Simple answer:** Security feature that prevents fake form submissions from other websites.

---

## 13. How do you handle form submissions?
Check if the request method is POST, create the form with POST data, validate, and process.

```python
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})
```

**Simple answer:** Check for POST, validate the form, save if valid, or show the form.

---

## 14. What are form widgets?
Widgets are the HTML elements that render form fields (text input, checkbox, select, etc.).

```python
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
```

**Simple answer:** Controls how form fields appear as HTML elements.

---

## 15. What is the `super()` block in templates?
`{{ block.super }}` displays the content from the parent block, letting you extend instead of replace.

```html
<!-- parent -->
{% block content %}
    <p>Parent content</p>
{% endblock %}

<!-- child -->
{% block content %}
    {{ block.super }}
    <p>Additional child content</p>
{% endblock %}
```

**Simple answer:** Keeps the parent's content and adds your own on top.

---

## 16. How do you create a custom template filter?
Create a `templatetags` folder in your app, add a Python file, and register the filter.

```python
# templatetags/my_filters.py
from django import template

register = template.Library()

@register.filter
def uppercase(value):
    return value.upper()
```

```html
{% load my_filters %}
{{ task.title|uppercase }}
```

**Simple answer:** Create a Python function and register it as a filter for use in templates.

---

## 17. What is the difference between `render()` and `redirect()`?
- **render()**: Returns a template with context (shows a page)
- **redirect()**: Sends the user to a different URL (after POST/DELETE)

```python
return render(request, 'task_list.html', {'tasks': tasks})  # Show page
return redirect('task_list')  # Go to URL
```

**Simple answer:** render displays a page; redirect sends the user elsewhere.

---

## 18. How do you pass multiple objects to a template?
Use a dictionary with multiple keys in the context.

```python
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    comments = task.comments.all()
    context = {
        'task': task,
        'comments': comments,
        'user': request.user,
    }
    return render(request, 'task_detail.html', context)
```

**Simple answer:** Put all data in a dictionary and pass it to render().

---

## 19. What are form field validators?
Validators check if form data meets specific requirements (email format, min length, etc.).

```python
from django.core.validators import MinLengthValidator, EmailValidator

class TaskForm(forms.Form):
    title = forms.CharField(
        validators=[MinLengthValidator(5)]
    )
    email = forms.EmailField()
```

**Simple answer:** Rules that check if entered data is valid (length, format, etc.).

---

## 20. How do you handle file uploads in forms?
Use `FileField` or `ImageField` in the form and set `enctype="multipart/form-data"` in the HTML.

```python
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'attachment']
```

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
</form>
```

**Simple answer:** Add file field to form and set special encoding in HTML.

---

# Project-Based Questions

## 21. Why use template inheritance?
Template inheritance keeps your HTML DRY (Don't Repeat Yourself). The base template has the common layout (header, footer, navigation), and child templates only define the unique content.

**Simple answer:** Avoid repeating the same HTML structure across multiple pages.

---

## 22. How do you handle form validation errors?
Display errors near the relevant fields and use CSS to highlight invalid fields. This guides users to fix mistakes.

**Simple answer:** Show clear error messages next to fields that have problems.

---

## 23. Why use ModelForm instead of regular Form?
ModelForm saves time by automatically generating fields based on your model. It also handles saving directly to the database.

**Simple answer:** Less code, automatic field generation, and direct database saving.

---

## 24. How do you implement pagination?
Use Django's Paginator class to split your QuerySet into pages. Pass the page object to the template and add navigation links.

**Simple answer:** Use Paginator to split data, then show page numbers and next/prev links.

---

## 25. Why use Django messages?
Messages provide user feedback after actions (success, error, warning). They persist across redirects, so users see notifications even after page changes.

**Simple answer:** Show helpful notifications to users after they do something.
