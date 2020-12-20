from django.contrib import admin
from Fouraso.models import  Person, Zone, Product,  Command, Stock


# Register your models here.
@admin.register(Zone)
class Zone(admin.ModelAdmin):
    models = Zone
    field = ['__all__']


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
        'created_at',
        )

    exclude = ['created_at', 'email',]

@admin.register(Product)
class Product(admin.ModelAdmin):
    models = Product
    field = ['__all__']

    list_display = (
        'name',
        'reference',
        )

    list_filter = ['name']

@admin.register(Command)
class Command(admin.ModelAdmin):
    models = Command
    field = ['__all__']

    list_display = (
        'qteCommande',
        'price_unitaire',
        'montant',
        )
    exclude = ['created_at']
    list_filter = ['created_at']


@admin.register(Stock)
class Stock(admin.ModelAdmin):
    models = Stock
    field = ['__all__']

    list_display = (
        'name_product',
        'qteEntry',
        'qteSort',
        'qteRest',
        'zone',

        )
    list_filter = ['zone']
    exclude = ['created_at', 'updated_at']


