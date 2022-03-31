from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm, LoginForm, RegisterForm



def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main page site', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form not valid'
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'form.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect("index")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()

        return render(request, "form.html", {"form": form})