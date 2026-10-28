from django.contrib import admin
from .models import Project, Task, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "description", "owner__username")
    readonly_fields = ("created_at", "updated_at")


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project",
        "assigned_to",
        "status",
        "priority",
        "due_date",
        "is_overdue",
    )
    list_filter = ("status", "priority", "project")
    search_fields = ("title", "description")
    date_hierarchy = "due_date"
    readonly_fields = ("created_at", "updated_at")
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("task", "author", "created_at")
    search_fields = ("content", "author__username")