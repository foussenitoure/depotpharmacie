# import time
from django.db import models
import datetime

# from django.db.models import Avg

# Create your models here.

############################################################

                   ### DATABASE PHARMACIE ###

############################################################


class Person(models.Model):
        STATUS = (
            ('GUICHET 1', 'Guichet 1'),
            ('GUICHET 2', 'Guichet 2'),
            ('CLIENT',    'Client'),
            ('PATIENT', 'Patient'),
            ('MEDECIN', 'Medecin'),
            ('REVENDEUR',   'Revendeur'),
            ('GESTIONNAIRE','Gestionnaire'),
            ('FOURNISSEUR', 'Fournisseur'),
            ('COMPANY',     'Company'),)

        status = models.CharField(max_length=30, choices=STATUS)
        # user = models.ForeignKey('User', on_delete=models.CASCADE)
        first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nom')
        last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Prénom')
        contact = models.CharField(max_length=50, null=True, blank=True, verbose_name='Numéro de Téléphone')
        email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='Adresse Email')
        created_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return ('{} - {} - {}').format(self.first_name, self.last_name, self.contact)


# class Zone(models.Model):
#         LOCALITE = (
#             ('ZANTIEBOUGOU', 'Zantiebougou'),
#             ('KATI FALADIE', 'Kati Faladie'),)
#         localite = models.CharField(max_length=30, choices=LOCALITE)
#
#         def __str__(self):
#             return self.localite

class Product(models.Model):
    REFERENCE = (
            ('GENERIQUE',  'GENERIQUE'),
            ('SPECIALITE', 'SPECIALITE'),)

    reference = models.CharField(max_length=30, choices=REFERENCE, default='GENERIQUE')
    name = models.CharField(max_length=100, blank=True, verbose_name='Nom du produit')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    # created_at = models.DateField(auto_now=True)

    def __str__(self):
        return ('{}{}').format(self.name, self.price,)

class Command(models.Model):
    LOCALITE = (
        ('ZANTIEBOUGOU', 'Zantiebougou'),
        ('KATI FALADIE', 'Kati Faladie'),)
    localite = models.CharField(max_length=30, choices=LOCALITE, verbose_name='Boutique', default='Zantiebougou')
    id_person = models.ForeignKey('Person', on_delete=models.CASCADE , verbose_name='Titulaire')
    product = models.ManyToManyField('Product')
    qteCommande = models.IntegerField(default=0, verbose_name='Quantite')
    submontant = models.DecimalField(decimal_places=2, max_digits=20, default=0, verbose_name='Sous Total')
    remise = models.DecimalField(decimal_places=2, max_digits=20, default=0, verbose_name='Remise')
    tva = models.DecimalField(decimal_places=2, max_digits=20, default=0, verbose_name='TVA')
    created_at = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Montant Total')

    def __str__(self):
        return ('{}').format(self.id,)
    # This code the montant is save in database
    # def  save(self):
    #      self.montant = self.qteCommande * self.price_unitaire
    #      return super(Command, self).save()

    # This code the montant is not save in database

    # @property
    # def montant(self, *args, **kwargs):
    #     montant = self.qteCommande * self.price
    #     return montant


class Stock(models.Model):
    name_product = models.ForeignKey('Product', on_delete=models.CASCADE)
    # zone = models.ForeignKey('Zone', on_delete=models.CASCADE)
    qteEntry = models.IntegerField(verbose_name='Quantité Entrée', default=0)
    qteSort = models.IntegerField(verbose_name='Quantite Sortie', default=0)
    qteRest = models.IntegerField(verbose_name='Quantite Restant', default=0)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now=True)

    # This code the show quantity product avaible is save in database
    def save(self, *args, **kwargs):
        self.qteRest = self.qteEntry - self.qteSort
        return super(Stock, self).save()

    # def __str__(self):
    #     return ('{}').format(self.qteRest)



        # var (qteCommande, price_unitaire, montant)
        # q   = qteCommande
        # p   = price_unitaire
        # m   = montant
        # # m   = q*p

        # return ('{} - {}').format(self.qteCommande, self.montant)
        # return ('{}').format(self.m)

# class example(models.Model):
#     var1 = models.IntegerField(default=0)
#     var2 = models.IntegerField(default=0)
#     var3 = models.IntegerField(default=0)
# DecimalField(decimal_places=2, max_digits=20)
#
#     sum = models.IntegerField(...)
#
#     def save(self):
#         self.sum = self.var1 + self.var2 + self.var3
#         return super(example, self).save()






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




