from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def home_view(request):
    """
    show all tasks for current user

    """
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'taskapp/home.html', context=context)


def create_task_view(request):
    """
    create task from form
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TaskForm()
    context = {'form': form}
    return render(request, 'taskapp/create_task.html', context=context)


def edit_task_view(request, id):
    """
    update current task
    """
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            redirect('home')
    form = TaskForm()
    context = {'form': form}
    return render(request,'taskapp/edit_task.html')


def delete_task(request, id):
    """
    delete task
    """
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')


def view_task(request, id):
    """
    view task
    """
    task = Task.objects.get(id=id)
    context = {'task': task}
    return render(request, 'taskapp/task.html', context=context)

