from django.contrib import admin

from .models import Promo, Contacts


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_published', 'show_main', 'discounts')
    list_display_links = ('pk', 'title', 'discounts')
    list_editable = ('is_published', 'show_main')
    search_fields = ('is_published', 'show_main')
    list_filter = ('is_published', 'show_main')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass
