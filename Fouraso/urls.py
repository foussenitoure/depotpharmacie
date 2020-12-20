from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('thanks/', views.thanks, name='thanks'),
    path('products/', views.products, name='products'),
    path('products/detail/<int:product_id>/', views.products_detail, name='products-detail'),

]
