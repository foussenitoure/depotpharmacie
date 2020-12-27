from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import context
from django.template import defaulttags
from Fouraso.form import ProductForm, StockForm
from Fouraso.models import Product, Stock




def thanks(request):
    return HttpResponse('Thanks, your form has been processed')

def products(request):
    if request.method == 'POST':

            # zon    = request.POST.get("zone")
            # cat    = request.POST.get("categorie")
            na      = request.POST.get("name")
            ref     = request.POST.get("reference")
            # pr     = request.POST.get("price")
            data   = Product(name=na, reference=ref,)
            data.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
       form = ProductForm()
    return render(request, 'Fouraso/products.html', {'form':form})


def products_detail(request, product_id):
    products = Product.objects.all()

    context = {

        'products': products
    }
    return render(request, 'Fouraso/products_list.html', context)


def about(request):
    # products = Product.objects.all()

    # context = {
    #
    #     'products': products
    # }
    return render(request, 'Fouraso/homepage.html',)


def stock(request,):
    Stocks = Stock.objects.all()
    form = StockForm()
    # context = {
    #     # 'stock': stock
    #
    # }
    return render(request, 'Fouraso/stock.html', {'form':form})

    # else:
    #    form = ProductForm()