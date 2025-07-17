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

class Category(models.Model):
    name = models.CharField(max_length=250)
