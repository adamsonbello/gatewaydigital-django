from django.shortcuts import render
from store.models import Product


def index(request):
     products = Product.objects.all().filter(is_available=True)
    

     context = {
       'products': products,
       
    }
     return render (request, 'pages/index.html', context)



def about(request):
   return render (request, 'pages/about.html')


def store(request):
    products = Product.object.all().filter(is_available=True)
    product_count = products.count()

    context = {
       'products': products,
       'product_count': product_count,
    }
    return render(request, 'store/store.html', {context})