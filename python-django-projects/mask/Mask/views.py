from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	context = {}
	return render(request, 'Mask/dashboard.html', context)


def products(request):
	products = Product.objects.all()
	return render(request, 'Mask/products.html', {'products':products})


