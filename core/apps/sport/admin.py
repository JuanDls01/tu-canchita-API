from django.contrib import admin
from .models import Sport


class SportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 25


admin.site.register(Sport, SportAdmin)
