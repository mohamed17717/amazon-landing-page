from django.contrib import admin

from .models import Product, ProductPicture, Coupon
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductPicture)
admin.site.register(Coupon)