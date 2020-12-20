from django import forms

class ProductForm(forms.Form):
    REFERENCE = (
            ('GENERIQUE',  'Générique'),
            ('SPECIALITE', 'Spécialite'),)

    reference           = forms.ChoiceField(choices=REFERENCE, required='Générique')
    name                = forms.CharField(label='Name', max_length=30)
    created_at          = forms.DateField()

# class ProductForm(forms.Form):
#
#     ZONE = (
#         ('ZONE_1', 'A'),
#         ('ZONE_2', 'B'),
#         ('ZONE_3', 'C'),)
#
#     zone = forms.ChoiceField(label='Zone', choices=ZONE, required='A')
#
#     CATEGORIE = (
#         ('FIL', 'Fil'),
#         ('AIGU', 'Aigu'),
#         ('SATIN', 'Satin'),
#         ('COL', 'Col'),)
#     categorie = forms.ChoiceField(label='Categorie', choices=CATEGORIE, required='Fil')
#     name      = forms.CharField(label='Name', max_length=30)
#     quantite  = forms.IntegerField(label='Quantite')
#     price     = forms.IntegerField(label='Prix')