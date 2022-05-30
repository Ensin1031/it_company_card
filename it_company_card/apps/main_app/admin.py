from django.contrib import admin

from .models import Promo, Contacts


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_published', 'show_main', 'discounts')
    list_display_links = ('pk', 'title', 'discounts')
    list_editable = ('is_published', 'show_main')
    search_fields = ('title',)
    list_filter = ('is_published', 'show_main')
    list_per_page = 10


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'reviewed', 'email_user', 'phone')
    list_display_links = ('pk', 'name', 'email_user', 'phone')
    list_editable = ('reviewed',)
    search_fields = ('name',)
    list_filter = ('reviewed',)
    list_per_page = 10


