from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task, Review
from . forms import TaskForm, CreateUserForm, LogInUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-user')
    context = {'form':form}
    return render(request, 'todo/register.html', context = context)


def loginUser(request):
    form = LogInUserForm()
    if request.method == 'POST':
        form = LogInUserForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)
                return redirect('all-task')
    context = {'form': form}
    return render(request, 'todo/login.html', context = context)


@login_required(login_url='login-user')
def logoutUser(request):
    auth.logout(request)
    return redirect('login-user')

@login_required(login_url='login-user')
def viewTask(request):
    quesryset = Task.objects.all()
    context = {'todos': quesryset}
    return render(request, 'todo/read_task.html', context)


@login_required(login_url='login-user')
def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-task')
    context = {'form': form}
    return render(request, 'todo/create_task.html', context)


@login_required(login_url='login-user')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('all-task')
    context = {'form': form, 'task': task}
    return render(request, 'todo/update_task.html', context)


@login_required(login_url='login-user')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('all-task')
