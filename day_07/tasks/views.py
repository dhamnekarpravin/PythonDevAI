from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "total_tasks": tasks.count(),
    }
    return render(request, "tasks/task_list.html", context)


def task_create(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully!")
            return redirect("task-list")

    context = {
        "form": form,
        "page_title": "Create Task",
    }
    return render(request, "tasks/task_form.html", context)


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect("task-list")

    context = {
        "form": form,
        "task": task,
        "page_title": "Edit Task",
    }
    return render(request, "tasks/task_form.html", context)


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect("task-list")

    context = {
        "task": task,
    }
    return render(request, "tasks/task_confirm_delete.html", context)