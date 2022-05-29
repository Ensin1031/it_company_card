from django.urls import path

from .views import ShowReviews, AddReview


urlpatterns = [
    path('', ShowReviews.as_view(), name='reviews'),
    path('add_review/', AddReview.as_view(), name='add_review'),
]
