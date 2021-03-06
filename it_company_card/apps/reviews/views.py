from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Reviews
from .forms import AddReviewForm


class ShowReviews(ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowReviews, self).get_context_data(**kwargs)
        context['breadcrumbs'] = (
            {'position': 1, 'name': 'Главная', 'url': 'home', 'resolved': True},
            {'position': 2, 'name': 'Все отзывы', 'resolved': False},
        )
        return context

    def get_queryset(self):
        return Reviews.objects.filter(status='OP')


class AddReview(LoginRequiredMixin, CreateView):
    form_class = AddReviewForm
    template_name = 'reviews/add_review.html'
    raise_exception = True
    success_url = reverse_lazy('reviews')

    def get_context_data(self, **kwargs):
        context = super(AddReview, self).get_context_data(**kwargs)
        context['breadcrumbs'] = (
            {'position': 1, 'name': 'Главная', 'url': 'home', 'resolved': True},
            {'position': 2, 'name': 'Все отзывы', 'url': 'reviews', 'resolved': True},
            {'position': 3, 'name': 'Добавить отзыв', 'resolved': False},
        )
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(AddReview, self).form_valid(form)
