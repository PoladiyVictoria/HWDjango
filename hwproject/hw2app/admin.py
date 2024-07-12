from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_num']
    ordering = ['name']
    list_filter = ['name', 'phone_num', 'address']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя клиента (name)'
    readonly_fields = ['date_reg']
    fieldsets = [
            (
            None,
            {
            'classes': ['wide'],
            'fields': ['name'],
            },
            ),
            (
            'Подробности',
            {
            'classes': ['collapse'],
            'description': 'Личные данные Клиента',
            'fields': ['email', 'phone_num', 'address'],
            },
            ),
            (
            'Дата регистрации',
            {
            'fields': ['date_reg'],
            }
            ),
            ]
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['price']
    list_filter = ['name', 'price', 'quantity', 'add_date']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    readonly_fields = ['add_date', 'path_to_image']
    fieldsets = [
            (
            None,
            {
            'classes': ['wide'],
            'fields': ['name'],
            },
            ),
            (
            'Подробности',
            {
            'classes': ['collapse'],
            'description': 'Подробные данные Продукта',
            'fields': ['description', 'price', 'quantity'],
            },
            ),
            (
            'Дополнительно',
            {
            'fields': ['add_date', 'path_to_image'],
            }
            ),
            ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']
    ordering = ['client', 'total_amount']
    list_filter = ['total_amount', 'order_date']
    search_fields = ['client']
    search_help_text = 'Поиск по полю Клиент (client)'
    readonly_fields = ['order_date']
    fieldsets = [
            (
            None,
            {
            'classes': ['wide'],
            'fields': ['client'],
            },
            ),
            (
            'Подробности',
            {
            'classes': ['collapse'],
            'description': 'Подробные данные Заказа',
            'fields': ['order', 'total_amount'],
            },
            ),
            (
            'Дата Заказа',
            {
            'fields': ['order_date'],
            }
            ),
            ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
