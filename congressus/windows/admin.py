from django.contrib import admin

from .models import TicketWindow
from .models import TicketWindowSale


class TicketWindowAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'event', 'location')
    list_filter = ('event', 'location')
    search_fields = ('name', 'slug', 'event__name')
    filter_horizontal = ('users', )


class TicketWindowSaleAdmin(admin.ModelAdmin):
    list_display = ('window', 'user', 'purchase', 'price', 'payment')
    list_filter = ('user', 'payment', 'window', 'window__event')
    search_fields = ('window__name', 'user__username', 'window__event__name')
    date_hierarchy = 'date'


admin.site.register(TicketWindow, TicketWindowAdmin)
admin.site.register(TicketWindowSale, TicketWindowSaleAdmin)