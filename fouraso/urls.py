from django.contrib import admin
from django.urls import path, re_path
from . import views


namespace = 'fouraso'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='homepage'),
    path('thanks/', views.thanks, name='thanks'),
    path('command/', views.command, name='command'),
    path('person/', views.person, name='persons'),
    re_path(r'^(?P<person_id>[0-9]+)/$', views.persons_detail, name='person_detail'),
    path('products/', views.products, name='products'),
    # path('products/', views.list_products, name='list_products'),
    re_path(r'^(?P<product_id>[0-9]+)/$', views.products_detail, name='products_detail'),
    path('stock/', views.stock, name='stock'),


]
