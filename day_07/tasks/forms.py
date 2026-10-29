from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "due_date"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Enter task title"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 4,
                    "placeholder": "Enter task details"
                }
            ),
            "due_date": forms.DateInput(
                attrs={
                    "class": "form-input",
                    "type": "date"
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if len(title.strip()) < 3:
            raise forms.ValidationError(
                "Task title must be at least 3 characters long."
            )

        return title.strip()