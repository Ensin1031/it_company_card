
import django_filters
from django_filters.widgets import RangeWidget

from .models import News


class NewsFilter(django_filters.FilterSet):
    """Класс фильтрации полей модели новостей"""

    order_from = django_filters.DateFromToRangeFilter(
        label='Введите даты сортировки:', method='filter_by_ordering', widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = News
        fields = ()

    def filter_by_ordering(self, queryset, name, value):
        if value.start and value.stop:
            sort_queryset = queryset.filter(date_create__gte=value.start, date_create__lte=value.stop)
        elif value.start and not value.stop:
            sort_queryset = queryset.filter(date_create__gte=value.start)
        elif value.stop and not value.start:
            sort_queryset = queryset.filter(date_create__lte=value.stop)
        else:
            sort_queryset = queryset
        return sort_queryset
