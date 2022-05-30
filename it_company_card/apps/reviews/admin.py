from django.contrib import admin

from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'user', 'deleted', 'status')
    list_display_links = ('pk', 'title')
    list_editable = ('status', 'deleted')
    list_filter = ('deleted', )
    search_fields = ('title',)
    list_per_page = 10

