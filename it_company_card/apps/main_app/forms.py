from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    '''Класс регистрации нового пользователя'''
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text='Имя пользователя должно быть!')
    email = forms.EmailField(label='Em@il', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text='Пароль должен быть ну ОЧЕНЬ секретным!!')
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    '''Класс аутентификации пользователя'''
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
