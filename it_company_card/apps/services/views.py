from django.views.generic import ListView, DetailView

from .models import Services, Category


class ShowServices(ListView):
    template_name = 'services/index.html'
    context_object_name = 'services'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowServices, self).get_context_data(**kwargs)
        if 'slug' in self.kwargs.keys():
            context['title'] = f'Все услуги в категории {Category.objects.filter(slug=self.kwargs["slug"]).first()}'
        else:
            context['title'] = f'Все услуги'
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
        if self.object.discounts:
            context['new_price'] = round((1 - self.object.discounts.discounts) * self.object.price, 2)
        return context

    def get_queryset(self):
        return Services.objects.filter(slug=self.kwargs['slug'])
