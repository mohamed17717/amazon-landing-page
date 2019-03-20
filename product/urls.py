from django.urls import path
from .views import (
  product_home_view,
  product_create_view,
  product_details_view,
  product_take_coupon_view,
)

app_name = 'product'

urlpatterns = [
  path('', product_home_view, name='product_home'),
  path('create/', product_create_view, name='product_create'),
  path('details/<slug:slug>/', product_details_view, name='product_details'),
  path('get-coupon/<slug:slug>/', product_take_coupon_view, name='product_coupon'),
]