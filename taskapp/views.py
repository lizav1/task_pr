from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import TaskForm


#login/registration view


def login_view(request):
    form = AuthenticationForm()
    # if request.method == "POST":
        #login logic
    context = {"form": form}
    return render(request, 'taskapp/login.html', context=context)


def signup_view(request):

    context = {"form": {}}
    return render(request, 'taskapp/signup.html', context=context)

def logout(request):
    #logout logic
    return redirect('home')

# view for task


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

