from django.urls import path

from .views import ShowServises


urlpatterns = [
    path('', ShowServises.as_view(), name='services'),
    # path('add_review/', AddReview.as_view(), name='add_review'),
]
