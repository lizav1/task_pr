from django.shortcuts import render
from .models import Task
from django.views.generic.detail import DetailView

def homeView(request):
    model = Task
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'taskapp/home.html', context=context)


class taskView(DetailView):
    model = Task
    template_name = 'taskapp/task.html'
