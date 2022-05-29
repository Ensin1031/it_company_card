from django import template
from django.db.models import Count, F

from apps.services.models import Category
from apps.main_app.models import Promo

register = template.Library()


@register.inclusion_tag('inc/_services_sidebar.html')
def show_services_sidebar():
    queryset = Category.objects.filter(presence=True).annotate(cnt=Count(
        'category_good', filter=F('category_good__presence')))
    promo = Promo.objects.filter(is_published=True)
    cont = {
        'category': queryset,
        'promo': promo,
    }
    return cont
