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

---

# Day 8: DRF Fundamentals - Interview Questions

## 26. What is Django REST Framework (DRF)?
DRF is a powerful toolkit for building Web APIs in Django. It provides serializers, viewsets, authentication, and other tools to create RESTful APIs easily.

```python
# Install DRF
pip install djangorestframework

# Add to INSTALLED_APPS
INSTALLED_APPS = [
    'rest_framework',
    'tasks',
]
```

**Simple answer:** A Django add-on that makes building APIs much easier.

---

## 27. What is a serializer?
A serializer converts complex data (like models) into JSON and vice versa. It handles validation and data transformation.

```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'priority']
```

**Simple answer:** Converts Python objects to JSON and JSON back to Python objects.

---

## 28. What is the difference between ModelSerializer and regular Serializer?
- **ModelSerializer**: Automatically generates fields based on a model
- **Serializer**: You manually define all fields

```python
# ModelSerializer - automatic
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# Regular Serializer - manual
class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    status = serializers.CharField()
```

**Simple answer:** ModelSerializer auto-generates from your model; regular Serializer requires manual field definition.

---

## 29. What is an APIView?
APIView is the base class for DRF views. It provides methods like get(), post(), put(), delete() for handling HTTP requests.

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskListAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

**Simple answer:** A class-based view with methods for each HTTP verb (GET, POST, etc.).

---

## 30. What are generic views in DRF?
Generic views are pre-built views that handle common patterns like list, create, retrieve, update, and delete operations.

```python
from rest_framework import generics

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

**Simple answer:** Ready-made views for common API operations, saving you from writing repetitive code.

---

## 31. What is a ViewSet?
A ViewSet combines multiple views (list, create, retrieve, update, delete) into a single class. It works with routers to automatically generate URLs.

```python
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

**Simple answer:** A single class that handles all CRUD operations for a model.

---

## 32. What is a router in DRF?
A router automatically generates URL patterns for your ViewSets, saving you from manually defining URLs.

```python
from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

**Simple answer:** Automatically creates URLs for your ViewSet so you don't have to write them manually.

---

## 33. What is the difference between APIView and ViewSet?
- **APIView**: You define methods (get, post, put, delete) and manually create URLs
- **ViewSet**: Combines multiple operations, works with routers for automatic URL generation

**Simple answer:** APIView gives you manual control; ViewSet is more automatic with routers.

---

## 34. How do you return JSON responses in DRF?
Use the Response class from DRF, which automatically converts data to JSON.

```python
from rest_framework.response import Response

def get(self, request):
    data = {'message': 'Hello'}
    return Response(data)  # Automatically JSON
```

**Simple answer:** Use DRF's Response class instead of Django's HttpResponse.

---

## 35. What is @api_view decorator?
The @api_view decorator converts a regular function-based view into an API view that handles content negotiation and authentication.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
```

**Simple answer:** Turns a regular function into an API view that can handle different HTTP methods.

---

## 36. What is the difference between ListAPIView and RetrieveAPIView?
- **ListAPIView**: Returns a list of objects (GET /tasks/)
- **RetrieveAPIView**: Returns a single object (GET /tasks/1/)

```python
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

**Simple answer:** List for multiple items; Retrieve for single item.

---

## 37. How do you handle validation in serializers?
DRF automatically validates based on field types. You can add custom validation with validate() or validate_<field>() methods.

```python
class TaskSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title too short")
        return value

    def validate(self, data):
        if data['status'] == 'completed' and not data.get('due_date'):
            raise serializers.ValidationError("Completed tasks need due date")
        return data
```

**Simple answer:** DRF auto-validates fields; add custom validation with validate methods.

---

## 38. What is status in DRF Response?
The status parameter sets the HTTP status code for the response.

```python
return Response(serializer.data, status=201)  # Created
return Response(serializer.errors, status=400)  # Bad Request
return Response({'error': 'Not found'}, status=404)  # Not Found
```

**Simple answer:** Sets the HTTP status code (200, 201, 400, 404, etc.) for the API response.

---

## 39. What are the main generic view classes in DRF?
- **ListAPIView**: List all objects
- **CreateAPIView**: Create new object
- **RetrieveAPIView**: Get single object
- **UpdateAPIView**: Update object
- **DestroyAPIView**: Delete object
- **ListCreateAPIView**: List and create
- **RetrieveUpdateDestroyAPIView**: Retrieve, update, delete

**Simple answer:** Pre-built views for each CRUD operation.

---

## 40. How do you serialize a single object vs a list?
Use `many=True` when serializing a list of objects.

```python
# Single object
task = Task.objects.get(id=1)
serializer = TaskSerializer(task)

# List of objects
tasks = Task.objects.all()
serializer = TaskSerializer(tasks, many=True)
```

**Simple answer:** Add many=True when serializing multiple objects.

---

## 41. What is the difference between @action decorator in ViewSets?
The @action decorator adds custom actions to a ViewSet beyond the standard CRUD operations.

```python
from rest_framework.decorators import action

class TaskViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'completed'
        task.save()
        return Response({'status': 'completed'})
```

**Simple answer:** Adds custom methods to your ViewSet for special operations.

---

## 42. How do you filter QuerySets in DRF views?
Filter the queryset in the view's get_queryset() method or use queryset attribute.

```python
class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
```

**Simple answer:** Filter in get_queryset() based on request parameters.

---

## 43. What is request.data in DRF?
request.data contains the parsed request body (JSON, form data, etc.). It's like request.POST but works for any content type.

```python
def post(self, request):
    # request.data automatically parses JSON/form data
    serializer = TaskSerializer(data=request.data)
```

**Simple answer:** The parsed data from the request body (works for JSON, forms, etc.).

---

## 44. How do you add DRF to an existing Django project?
1. Install DRF: `pip install djangorestframework`
2. Add to INSTALLED_APPS in settings.py
3. Create serializers
4. Create API views or ViewSets
5. Configure URLs

**Simple answer:** Install, add to apps, create serializers and views, set up URLs.

---

## 45. What is the purpose of serializers in DRF?
Serializers handle:
- Converting models to JSON (serialization)
- Converting JSON to models (deserialization)
- Data validation
- Error handling

**Simple answer:** They convert between Python objects and JSON while validating data.

---

# Project-Based Questions

## 46. Why use ViewSets instead of APIViews?
ViewSets reduce code duplication by combining multiple views (list, create, retrieve, update, delete) into one class. Routers automatically generate URLs, saving time.

**Simple answer:** Less code, automatic URL generation, and better organization.

## 47. How do you create a CRUD API with DRF?
Use ModelViewSet with a ModelSerializer and a router. This gives you full CRUD with minimal code.

```python
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

router.register('tasks', TaskViewSet)
```

**Simple answer:** ModelViewSet + ModelSerializer + router = full CRUD API.

## 48. Why use serializers instead of returning model objects directly?
Serializers control what data is exposed, handle validation, and convert to JSON format. They provide security by not exposing sensitive fields.

**Simple answer:** Control what data is sent, validate input, and convert to proper JSON format.

## 49. How do you handle errors in DRF?
DRF automatically returns validation errors in a consistent JSON format. You can also raise exceptions like ValidationError or NotFound.

```python
if not task:
    raise NotFound("Task not found")
```

**Simple answer:** DRF auto-handles validation errors; use exceptions for custom error cases.

## 50. What is the difference between generics and ViewSets?
- **Generics**: Individual views for specific operations (list, create, etc.)
- **ViewSets**: All operations in one class with automatic URL routing

**Simple answer:** Generics are separate views; ViewSets combine everything with routers.
