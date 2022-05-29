from django.urls import path

from .views import ShowNews, ViewPost


urlpatterns = [
    path('', ShowNews.as_view(), name='news_index'),
    path('post/<str:slug>/', ViewPost.as_view(), name='post'),
]
