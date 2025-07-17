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
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return self.name

