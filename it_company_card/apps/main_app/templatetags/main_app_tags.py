from django import template

from apps.main_app.models import Banners
from apps.news.models import News

register = template.Library()


@register.inclusion_tag('inc/_main_news.html')
def show_main_news():
    queryset = News.objects.filter(is_published=True)[:3]
    return {'news': queryset}


@register.inclusion_tag('inc/_main_banners.html')
def show_banners():
    queryset = Banners.objects.filter(is_published=True)[:2]
    return {'banners': queryset}
