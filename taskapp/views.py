from django.shortcuts import render, redirect
from .models import Task, TaskStatus
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import TaskForm



#login/registration views

def login_view(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return {} #add message
    context = {"form": form}
    return render(request, 'taskapp/login.html', context=context)


def signup_view(request):
    """
    register new user
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("home")
        else:
            #print error
             return {}
    context = {"form": UserCreationForm}
    return render(request, 'taskapp/signup.html', context=context)


def logout_event(request):
    logout(request)
    return redirect('home')


# view for tasks


@login_required(login_url="login")
def home_view(request):
    """
    show all tasks for current user with filters by status
    """
    # add id for view
    # status filter my / my to do filter

    status = TaskStatus.objects.all()
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'status': status}
    return render(request, 'taskapp/home.html', context=context)


@login_required(login_url="login")
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


@login_required(login_url="login")
def edit_task_view(request, id):
    """
    update current task information
    """
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.instance.edited = True
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'taskapp/edit_task.html', context=context)


@login_required(login_url="login")
def delete_task(request, id):
    """
    delete task
    """
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')


@login_required(login_url="login")
def view_task(request, id):
    """
    view task
    """
    task = Task.objects.get(id=id)
    context = {'task': task}
    return render(request, 'taskapp/task.html', context=context)


@login_required(login_url="login")
def profile_view(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request,'taskapp/profile.html',context=context)