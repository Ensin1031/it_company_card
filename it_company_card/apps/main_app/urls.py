from django.urls import path

from .views import index, register, user_login, user_logout


urlpatterns = [
    path('', index, name='home'),
    path('main_app/register/', register, name='register'),
    path('main_app/login/', user_login, name='login'),
    path('main_app/logout/', user_logout, name='logout'),
]
