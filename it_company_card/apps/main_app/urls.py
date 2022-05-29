from django.urls import path

from .views import index, register, user_login, user_logout, ShowPromo, ShowContacts


urlpatterns = [
    path('', index, name='home'),
    path('promo/<str:slug>', ShowPromo.as_view(), name='promo'),
    path('contacts/', ShowContacts.as_view(), name='contacts'),
    path('main_app/register/', register, name='register'),
    path('main_app/login/', user_login, name='login'),
    path('main_app/logout/', user_logout, name='logout'),
]
