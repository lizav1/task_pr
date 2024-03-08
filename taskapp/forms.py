from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    """
    form for creating new form
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'assignee']