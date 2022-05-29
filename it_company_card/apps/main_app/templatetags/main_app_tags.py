from django import template

from apps.main_app.models import Promo
from apps.news.models import News
from apps.services.models import Services

register = template.Library()


@register.inclusion_tag('inc/_main_news.html')
def show_main_news():
    queryset = News.objects.filter(is_published=True)[:3]
    return {'news': queryset}


@register.inclusion_tag('inc/_main_banners.html')
def show_banners():
    queryset = Promo.objects.filter(is_published=True)[:2]
    return {'banners': queryset}


@register.inclusion_tag('inc/_main_services.html')
def show_main_services():
    queryset = Services.objects.filter(show_main=True)[:3]
    return {'services': queryset}
