from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    products=Product.objects.all()
    return render(request, "products/products.html", {'listProduct':products})