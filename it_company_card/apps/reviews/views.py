from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from .models import Reviews


class ShowReviews(ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowReviews, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Reviews.objects.filter(status='OP')


class AddReview(LoginRequiredMixin, CreateView):
    model = Reviews
    template_name = 'reviews/add_review.html'
