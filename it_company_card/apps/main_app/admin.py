from django.contrib import admin

from .models import Banners


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    pass
