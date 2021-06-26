from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='homepage'),
    path('thanks/', views.thanks, name='thanks'),
    path('command/', views.command, name='command'),
    path('person/', views.person, name='person'),
    path('person/detail/<int:person_id>/', views.persons_detail, name='person-detail'),
    path('products/', views.products, name='products'),
    path('products/detail/<int:product_id>/', views.products_detail, name='products-detail'),
    path('stock/', views.stock, name='stock'),
    # path('zone/', views.zone, name='zone'),

]
