from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import RegisterUserForm, LoginUserForm


def index(request):
    return render(request, 'main_app/index.html', {'title': 'Hello, main'})


def register(request):
    """Функция регистрации нового пользователя"""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegisterUserForm()

    cont = {
        'title': 'Регистрация нового пользователя',
        'form': form
    }
    return render(request, 'main_app/register.html', cont)


def user_login(request):
    """Функция авторизации зарегистрированного пользователя"""
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginUserForm()

    cont = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'main_app/login.html', cont)


def user_logout(request):
    """Функция логаута для аутентифицированного пользователя"""
    logout(request)
    return redirect('login')
