import time
from django.db import models
import datetime

from django.db.models import Avg

# Create your models here.

############################################################

                   ### DATABASE PHARMACIE ###

############################################################


class Person(models.Model):
        STATUS       = (
            ('CLIENT',      'Client'),
            ('REVENDEUR',   'Revendeur'),
            ('GESTIONNAIRE','Gestionnaire'),
            ('MEDECIN',     'Medecin'),
            ('PATIENT',     'Patient'),
            ('FOURNISSEUR', 'Fournisseur'),
            ('COMPANY',     'Company'),)

        status       = models.CharField(max_length=30, choices=STATUS)
        first_name   = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nom')
        last_name    = models.CharField(max_length=50, null=True, blank=True, verbose_name='Prénom')
        contact      = models.CharField(max_length=50, null=True, blank=True, verbose_name='Numéro de Téléphone')
        email        = models.EmailField(max_length=50, null=True, blank=True, verbose_name='Adresse Email')
        created_at   = models.DateTimeField(auto_now=True)

        def __str__(self):
            return ('{} - {} - {}').format(self.first_name, self.last_name, self.contact)

class Zone(models.Model):
        LOCALITE = (
            ('ZANTIEBOUGOU', 'Zantiebougou'),
            ('KATI FALADIE', 'Kati Faladie'),)
        localite = models.CharField(max_length=30, choices=LOCALITE)

        def __str__(self):
            return self.localite

class Product(models.Model):

    REFERENCE   = (
            ('GENERIQUE',  'GENERIQUE'),
            ('SPECIALITE', 'SPECIALITE'),)

    reference     = models.CharField(max_length=30, choices=REFERENCE, default='GENERIQUE')
    name          = models.CharField(max_length=100, blank=True, verbose_name='Nom du produit')
    created_at    = models.DateField(auto_now=True)

    def __str__(self):
        return ('{}-{}').format(self.name, self.reference)


class Stock(models.Model):
    name_product         = models.ForeignKey('Product', on_delete=models.CASCADE)
    zone                 = models.ForeignKey('Zone', on_delete=models.CASCADE)
    qteEntry             = models.IntegerField(verbose_name='Quantité Entrée')
    qteSort              = models.IntegerField(verbose_name='Quantite Sortie')
    qteRest              = models.IntegerField(verbose_name='Quantite Restant')
    updated_at           = models.DateField()
    created_at           = models.DateField()

    def __str__(self):
        return ('{}').format(self.qteRest)

class Command(models.Model):
    person                   = models.ForeignKey('Person', on_delete=models.CASCADE)
    product                  = models.ManyToManyField('Product')
    qteCommande              = models.IntegerField(verbose_name='Quantité')
    price_unitaire           = models.DecimalField(decimal_places=2, max_digits=20)
    montant                  = models.DecimalField(decimal_places=2, max_digits=20)
    created_at               = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ('{} - {}').format(self.qteCommande, self.montant)








# class Entry(models.Model):
#     name                  = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
#     Quantite              = models.IntegerField(verbose_name='Quantité')
#     Observation           = models.TextField(max_length=500, null=True, blank=True, verbose_name='Observation')
#     created_at            = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return ('{}').format(self.name)
#
#
# class Sort(models.Model):
#     Nom_Agent             = models.ForeignKey('People', on_delete=models.DO_NOTHING, verbose_name='Nom Agent')
#     Designation_Product   = models.ManyToManyField('Product')
#     Quantite              = models.IntegerField(blank=True, null=False, verbose_name='Quantité')
#     created_at            = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return ('{}').format(self.Nom_Agent)
#
#
# class Inventaire(models.Model):
#     type_product            = models.ForeignKey('Product' , on_delete=models.DO_NOTHING,)
#     Qentre                  = models.ForeignKey('Entry' , on_delete=models.DO_NOTHING,)
#     Qsort                   = models.ForeignKey('Sort' , on_delete=models.DO_NOTHING,)
#
#     created_at              = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#        return  ('{} - {} - {}').format(self.type_product, self.Qentre, self.Qsort)

# class Stock(models.Model):
#
#     zone                = models.ForeignKey('Zone', on_delete=models.CASCADE,
#                                                verbose_name="Point de Vente",)
#     # products          = models.ForeignKey('Productt', on_delete=models.DO_NOTHING,
#     #                                            verbose_name="Produits",)
#
#     entree_product      = models.ManyToManyField('Productt', verbose_name=' La liste des produits')
#     # Designation_Product = models.CharField(max_length=30,  blank=True, verbose_name='Designation produit')
#     QteEntry            = models.IntegerField(verbose_name='Quantité Entrée')
#     QteStock            = models.IntegerField(verbose_name='Quantité de Stock')
#     sortie              = models.IntegerField(verbose_name='Quantite Sortie')
#     restant             = models.IntegerField(verbose_name='Quantite Restant')
#     price               = models.DecimalField(decimal_places=2, max_digits=20, default=45.99)
#     created_at          = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return ('{} - {}').format(self.QteEntry, self.QteStock)




