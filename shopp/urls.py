from django.urls import path
from .views import home, productView, productsAdd, updateProductView, searchView

app_name = "shopp"

urlpatterns = [
    path("", home, name="dashboard"),
    path("products/", productView, name="products"),
    path("products/add/", productsAdd, name="products-add"),
    path("update/<str:slug>", updateProductView, name="products-update"),
    path("search/", searchView, name="searches")
]