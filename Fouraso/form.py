from django import forms
# from django.core.exceptions import ValidationError


class PersonForm(forms.Form):
    STATUS = (
            ('CLIENT', 'Client'),
            ('REVENDEUR', 'Revendeur'),
            ('GESTIONNAIRE', 'Gestionnaire'),
            ('MEDECIN', 'Medecin'),
            ('PATIENT', 'Patient'),
            ('FOURNISSEUR', 'Fournisseur'),
            ('COMPANY', 'Company'),)

    status = forms.ChoiceField(choices=STATUS,)
    first_name = forms.CharField(max_length=50,   label='Nom')
    last_name = forms.CharField(max_length=50,   label='Prenom')
    contact = forms.CharField(max_length=50,   label='Numero de Telephone')
    email = forms.EmailField(max_length=50,   label='Adresse Email')
    created_at = forms.DateTimeField()


# class ZoneForm(forms.Form):
#     LOCALITE = (
#         ('ZANTIEBOUGOU', 'Zantiebougou'),
#         ('KATI FALADIE', 'Kati Faladie'),)
#     localite = forms.ChoiceField(choices=LOCALITE)


class ProductForm(forms.Form):
    REFERENCE = (
            ('GENERIQUE',  'Generique'),
            ('SPECIALITE', 'Specialite'),)

    reference = forms.ChoiceField(choices=REFERENCE, required='Generique')
    name = forms.CharField(label='Name', max_length=30)
    price = forms.DecimalField(label='Prix')
    # created_at          = forms.DateTimeField()


class CommandForm(forms.Form):
    LOCALITE = (
                ('ZANTIEBOUGOU', 'Zantiebougou'),
                ('KATI FALADIE', 'Kati Faladie'),)
    localite = forms.ChoiceField(choices=LOCALITE)
    # person                   =  forms.ForeignKey('Person',)
    # product                  =  forms.ManyToManyField('Product')
    qteCommande = forms.IntegerField(label='Quantite Commande')
    submontant = forms.DecimalField()
    remise = forms.DecimalField(label='REMISE')
    tva = forms.DecimalField(label='TVA')
    created_at = forms.DateTimeField(label='Date commande')
    montant = forms.IntegerField(label='Montant Total')

    # This function for clean fields commands

    # def clean_qteCommande(self):
    #     data = self.cleaned_data['qteCommande']
    #     if " 0 " not in data:
    #         raise ValidationError("You have forgotten about Fred!")

    # Always return a value to use as the new cleaned data, even if
    # this method didn't change it.
    # return data


class StockForm(forms.Form):
    name_product = forms.CharField(label='Nom produit')
    zone = forms.CharField(label='Zone')
    qteEntry = forms.IntegerField(label='Quantite Entree')
    qteSort = forms.IntegerField(label='Quantite Sortie')
    qteRest = forms.IntegerField(label='Quantite Restant')
    updated_at = forms.DateField()
    created_at = forms.DateField()
