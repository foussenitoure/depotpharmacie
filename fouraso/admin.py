from django.contrib import admin
from fouraso.models import Person,  Product,  Command, Stock
# Zone,

# Register your models here.
# @admin.register(Zone)
# class Zone(admin.ModelAdmin):
#     models = Zone
#     field = ['__all__']


@admin.register(Person)
class Person(admin.ModelAdmin):
    models = Person
    field = ['__all__']

    list_display = (
        'status',
        'first_name',
        'last_name',
        'contact',
        'email',
        'created_at',)
    list_filter = ['status']
    exclude = ['created_at', 'email']


@admin.register(Product)
class Product(admin.ModelAdmin):
    models = Product
    field = ['__all__']

    list_display = (
        'name',
        'reference',
        'price',)

    list_filter = ['name']
    exclude = ['created_at']


@admin.register(Command)
class Command(admin.ModelAdmin):
    models = Command
    field = ['__all__']

    list_display = (
        # 'person',
        # 'product',
        'localite',
        # 'qteCommand',
        'submontant',
        'remise',
        'tva',
        'montant',
        'codeCommand',)
    exclude = ['created_at']
    ordering = ['created_at']
    list_filter = ['created_at', 'localite','codeCommand',]


@admin.register(Stock)
class Stock(admin.ModelAdmin):
    models = Stock
    field = ['__all__']

    list_display = (
        'name_product',
        'qteEntry',
        'qteSort',
        'qteRest',)
    # list_filter = ['zone']
    exclude = ['created_at', 'updated_at']
