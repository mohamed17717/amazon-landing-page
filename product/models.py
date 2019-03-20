from django.db import models
from django.urls import  reverse
from django.utils.text import slugify
from django.core.exceptions import FieldError

from .scripts.ScrapeAmazon import AmazonScraper
from time import time
from pprint import pprint
# Create your models here.
class Coupon(models.Model):
	## from user
	code 				= models.CharField(max_length=50)
	howlong 		= models.SmallIntegerField() # input in hours
	howmany 		= models.SmallIntegerField()
	salepercent = models.SmallIntegerField()
	## computed
	start_time 	= models.FloatField(blank=True)
	end_time 		= models.FloatField(blank=True)
	used 				= models.SmallIntegerField(default=0)
	left 				= models.SmallIntegerField(blank=True)

	def save(self, *args, **kwargs):
		self.left = self.howmany - self.used
		if not self.end_time:
			self.start_time = time()
			self.howlong *= 60*60 # convert to sceonds
			self.end_time = self.start_time + self.howlong

		super(Coupon, self).save(*args, **kwargs)

class ProductPicture(models.Model):
	small_picture = models.URLField(max_length=350)
	large_picture = models.URLField(max_length=350)

class Product(models.Model):
	## from user
	amazon_url 	= models.URLField(max_length=350)
	coupon 			= models.ForeignKey(Coupon, on_delete=models.CASCADE, blank=True, null=True)

	## conputed
	title 			= models.CharField(max_length=400, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	price 			= models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
	pictures 		= models.ManyToManyField(ProductPicture, blank=True)

	slug 				= models.SlugField(blank=True, null=True)

	class Meta:
		verbose_name = ("Product")
		verbose_name_plural = ("Products")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('product:product_details', kwargs={'slug': self.slug})



