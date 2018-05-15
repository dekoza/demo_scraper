from django.contrib import admin
from . import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']


@admin.register(models.Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['currency', 'date', 'value']
    date_hierarchy = 'date'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('currency')
