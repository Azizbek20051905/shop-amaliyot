from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField

# Create your models here.
class CustomeUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Super Admin"),
        ("seller", "Seller")
    ]
    image = models.ImageField(upload_to="profile/")
    role = models.CharField(max_length=40, choices=ROLE_CHOICES, default="seller")

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="name") 

    def __str__(self):
        return self.name

class Product(models.Model):
    TYPE_CHOICES = [
        ("dona", "Dona"),
        ("kg", "Kg")
    ]
    WHOLE_CHOICES = [
        ("block", "Block"),
        ("karobka", "Karobka")
    ]
    
    image = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=60, choices=TYPE_CHOICES, default='dona')
    amount = models.IntegerField(default=0)
    started_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    wholesale = models.CharField(max_length=50, choices=WHOLE_CHOICES, null=True, blank=True)
    blockAmount = models.IntegerField(default=0, null=True, blank=True)
    blockPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Add Cart: {self.product.name}"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    started_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Add Cart: {self.product.name}"
    

