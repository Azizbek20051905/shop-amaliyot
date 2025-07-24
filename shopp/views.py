from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def productView(request):
    return render(request, 'product.html')

def productsAdd(request):
    return render(request, 'add_product.html')

