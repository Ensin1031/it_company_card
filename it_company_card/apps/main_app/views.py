from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from .forms import RegisterUserForm, LoginUserForm
from .models import Promo


def index(request):
    return render(request, 'main_app/index.html')


class ShowPromo(DetailView):
    template_name = 'main_app/promo.html'
    context_object_name = 'promo'

    def get_context_data(self, **kwargs):
        context = super(ShowPromo, self).get_context_data(**kwargs)
        context['title'] = 'Информация по акции "' + str(self.object.title) + '"'
        context['disc'] = int(self.object.discounts * 100)
        return context

    def get_queryset(self):
        return Promo.objects.filter(is_published=True)


class ShowContacts(CreateView):
    pass


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
