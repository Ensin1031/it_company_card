from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_published', 'date_create')
    list_display_links = ('pk', 'title')
    readonly_fields = ('date_create', 'slug')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_per_page = 10
