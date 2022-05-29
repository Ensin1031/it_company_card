from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import News
from .filter import NewsFilter


class ShowNews(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowNews, self).get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ViewPost(DetailView):
    template_name = 'news/post.html'
    context_object_name = 'news_post'

    def get_context_data(self, **kwargs):
        context = super(ViewPost, self).get_context_data(**kwargs)
        context['title'] = f'Детали новости "{self.object}"'
        return context

    def get_queryset(self):
        return News.objects.filter(slug=self.kwargs['slug'])
