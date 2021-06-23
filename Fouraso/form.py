from django import forms


class PersonForm(forms.Form):
    STATUS = (
            ('CLIENT', 'Client'),
            ('REVENDEUR', 'Revendeur'),
            ('GESTIONNAIRE', 'Gestionnaire'),
            ('MEDECIN', 'Medecin'),
            ('PATIENT', 'Patient'),
            ('FOURNISSEUR', 'Fournisseur'),
            ('COMPANY', 'Company'),)

    status           = forms.ChoiceField(choices=STATUS,)
    first_name       = forms.CharField(max_length=50,   label='Nom')
    last_name        = forms.CharField(max_length=50,   label='Prenom')
    contact          = forms.CharField(max_length=50,   label='Numero de Telephone')
    email            = forms.EmailField(max_length=50,   label='Adresse Email')
    created_at       = forms.DateTimeField()


class ZoneForm(forms.Form):
    LOCALITE = (
        ('ZANTIEBOUGOU', 'Zantiebougou'),
        ('KATI FALADIE', 'Kati Faladie'),)
    localite = forms.ChoiceField(choices=LOCALITE)


class ProductForm(forms.Form):
    REFERENCE = (
            ('GENERIQUE',  'Generique'),
            ('SPECIALITE', 'Specialite'),)

    reference           = forms.ChoiceField(choices=REFERENCE, required='Generique')
    name                = forms.CharField(label='Name', max_length=30)
    # created_at          = forms.DateTimeField()
    
    
    
class StockForm(forms.Form):
    name_product         = forms.CharField(label='Nom produit')
    zone                 = forms.CharField(label='Zone')
    qteEntry             = forms.IntegerField(label='Quantite Entree')
    qteSort              = forms.IntegerField(label='Quantite Sortie')
    qteRest              = forms.IntegerField(label='Quantite Restant')
    updated_at           = forms.DateField()
    created_at           = forms.DateField()




class CommandForm(forms.Form):
    # person                   =  forms.ForeignKey('Person',)
    # product                  =  forms.ManyToManyField('Product')
    qteCommande              =  forms.IntegerField(label='Quantite Commande')
    price_unitaire           =  forms.IntegerField(label='Prix Unitaire')
    created_at               =  forms.DateTimeField(label='Date commande')
    montant                  =  forms.IntegerField(label='Montant Total')


# class ProductForm(forms.Form):
#
#     ZONE = (
#         ('ZONE_1', 'A'),
#         ('ZONE_2', 'B'),
#         ('ZONE_3', 'C'),)
#
#     zone = forms.ChoiceField(label='Zone', choices=ZONE, required='A')
#
#  j   CATEGORIE = (
#         ('FIL', 'Fil'),
#         ('AIGU', 'Aigu'),
#         ('SATIN', 'Satin'),
#         ('COL', 'Col'),)
#     categorie = forms.ChoiceField(label='Categorie', choices=CATEGORIE, required='Fil')
#     name      = forms.CharField(label='Name', max_length=30)
#     quantite  = forms.IntegerField(label='Quantite')
#     price     = forms.IntegerField(label='Prix')