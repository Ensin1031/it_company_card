from django.urls import path

from .views import ShowServices, ShowService


urlpatterns = [
    path('', ShowServices.as_view(), name='services'),
    path('add_review/<str:slug>/', ShowService.as_view(), name='service'),
    path('services_for_category/<str:slug>/', ShowServices.as_view(), name='services_by_category'),
]
