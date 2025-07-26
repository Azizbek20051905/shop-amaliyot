from django.urls import path
from .views import home, productView, productsAdd

app_name = "shopp"

urlpatterns = [
    path("", home, name="dashboard"),
    path("products", productView, name="products"),
    path("products/add/", productsAdd, name="products-add")
]