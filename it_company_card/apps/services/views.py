from django.views.generic import ListView, DetailView

from .models import Services, Category


class ShowServices(ListView):
    template_name = 'services/index.html'
    context_object_name = 'services'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowServices, self).get_context_data(**kwargs)
        if 'slug' in self.kwargs.keys():
            cats = Category.objects.filter(slug=self.kwargs["slug"]).first()
            context['title'] = f'Все услуги в категории {cats}'
            context['breadcrumbs'] = (
                {'position': 1, 'name': 'Главная', 'url': 'home', 'resolved': True},
                {'position': 2, 'name': 'Все услуги', 'url': 'news_index', 'resolved': True},
                {'position': 3, 'name': f'Услуги категории "{cats}"', 'resolved': False},
            )
        else:
            context['title'] = f'Все услуги'
            context['breadcrumbs'] = (
                {'position': 1, 'name': 'Главная', 'url': 'home', 'resolved': True},
                {'position': 2, 'name': 'Все услуги', 'resolved': False},
            )
        return context

    def get_queryset(self):
        if 'slug' in self.kwargs.keys():
            queryset = Services.objects.filter(presence=True).filter(
                category__slug=self.kwargs['slug']).select_related('category')
        else:
            queryset = Services.objects.filter(presence=True).select_related('category')
        return queryset


class ShowService(DetailView):
    template_name = 'services/show_service.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super(ShowService, self).get_context_data(**kwargs)
        context['title'] = 'Просмотреть услугу "' + str(self.object.title) + '"'
        context['breadcrumbs'] = (
            {'position': 1, 'name': 'Главная', 'url': 'home', 'resolved': True},
            {'position': 2, 'name': 'Все услуги', 'url': 'services', 'resolved': True},
            {'position': 3, 'name': f'Услуга "{self.object.title}"', 'resolved': False},
        )
        if self.object.discounts:
            context['new_price'] = round((1 - self.object.discounts.discounts) * self.object.price, 2)
        return context

    def get_queryset(self):
        return Services.objects.filter(slug=self.kwargs['slug'])
