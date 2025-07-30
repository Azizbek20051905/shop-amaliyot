from django.shortcuts import render, redirect
from .models import Category, Product

# Create your views here.
def home(request):
    return render(request, "index.html")

def productView(request):
    products = Product.objects.all()

    context = {
        "products":products
    }
    return render(request, 'product.html', context)

def updateProductView(request, slug):
    product = Product.objects.get(slug=slug)
    category = Category.objects.all()
    
    context = {
        "page": "update",
        'product': product,
        "categories": category
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
        
        product.name = name
        product.category = category_add
        product.old_price = old_price
        product.sell_price = sell_price
        product.type = productType
        product.amount = amount
        product.wholesale = convertWhole
        product.blockAmount = convertAmount
        product.blockPrice = convertPrice
        
        if image:
            product.image = image
        
        product.save()

        return redirect("shopp:products")
    
    return render(request, 'add_product.html', context)

def productsAdd(request):
    categories = Category.objects.all()
    context = {
        'page':"add",
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

    return render(request, 'add_product.html', context)

