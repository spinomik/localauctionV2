from django.contrib import admin
from .models import Item
# Register your models here.


@admin.action(description='Zmień status na zakończone')
def close_auction(modeladmin, request, queryset):
    queryset.update(status='finished')

@admin.action(description='Zmień status na nowe')
def open_auction(modeladmin, request, queryset):
    queryset.update(status='new')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'shortDescription', 'picture', 'startDate', 'endDate',
                    'status', 'winner', 'maxPrice', 'voteDate']
    actions = [close_auction, open_auction]
