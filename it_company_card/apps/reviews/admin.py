from django.contrib import admin

from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass
