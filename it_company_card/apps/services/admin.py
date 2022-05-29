from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Services, Category


class ServiceInLine(admin.TabularInline):
    fk_name = 'category'
    model = Services


# @admin.register(Services)
# class ServicesAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'title', 'presence', 'show_main', 'category', 'price', 'n_views', 'discounts',)
#     list_display_links = ('pk', 'title', 'n_views')
#     list_editable = ('presence', 'show_main', 'discounts', 'category')
#     readonly_fields = ('n_views',)
#     search_fields = ('presence', 'show_main', 'discounts', 'n_views', 'category')
#     list_filter = ('presence', 'show_main', 'discounts', 'n_views', 'category')


@admin.register(Category)
class Category(DraggableMPTTAdmin):
    inlines = (ServiceInLine,)
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)

