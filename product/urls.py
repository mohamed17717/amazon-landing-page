from django.urls import path
from .views import (
  product_home_view,
  product_create_view,
  product_details_view,
  ProductDetailView,
)

app_name = 'product'

urlpatterns = [
  path('', product_home_view, name='product_home'),
  path('create/', product_create_view, name='product_create'),
  path('details/<slug:slug>/', ProductDetailView.as_view(), name='product_details'),
]