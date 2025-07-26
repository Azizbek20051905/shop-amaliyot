from django.shortcuts import render, redirect
from .models import Category, Product

# Create your views here.
def home(request):
    return render(request, "index.html")

def productView(request):
    return render(request, 'product.html')

def productsAdd(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }

    if request.method == "POST":
        image = request.FILES.get('imageInput')
        name = request.POST.get('NameInput')
        category = request.POST['category']
        category_name = request.POST['addCategory']
        old_price = request.POST['OldPriceInput']
        sell_price = request.POST['SellPriceInput']
        amount = request.POST['AmountInput']
        productType = request.POST['ProductType']
        convertWhole = request.POST['ConvertWholeInput']
        convertAmount = request.POST['ConvertAmountInput']
        convertPrice = request.POST['ConvertPriceInput']

        if not category:
            if category_name:
                category_add = Category.objects.create(name=category_name)
                category_add.save()
        else:
            category_add = Category.objects.get(slug=category)
        
        product_add = Product.objects.create(name=name, category=category_add, 
                                             old_price=old_price, 
                                             sell_price=sell_price, 
                                             type=productType,
                                             amount=amount,
                                             wholesale=convertWhole,
                                             blockAmount=convertAmount,
                                             blockPrice=convertPrice,
                                             image=image)
        product_add.save()

        return redirect("shopp:products")

    return render(request, 'add_product.html')

