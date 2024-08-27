from django.contrib import admin
from network.models import Network, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ-панель товара"""
    list_display = ('name', 'model', 'supplier', 'release_date')


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """Админ-панель звена сети"""
    list_filter = ['city', 'level']
    list_display = ['name', 'city', 'debt', 'level']
    actions = ['clear_debt']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)
