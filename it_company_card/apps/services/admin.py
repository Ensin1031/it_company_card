from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Services, Category


class ServiceInLine(admin.TabularInline):
    fk_name = 'category'
    model = Services


@admin.register(Category)
class Category(DraggableMPTTAdmin):
    inlines = (ServiceInLine,)
    list_display = ('tree_actions', 'indented_title', 'presence', 'title')
    list_display_links = ('indented_title',)
    list_filter = ('presence',)
    list_editable = ('presence',)
    search_fields = ('title',)
    list_per_page = 10
