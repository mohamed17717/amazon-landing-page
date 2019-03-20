from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify
from django.urls import reverse
from django.views.generic import DetailView

from pprint import pprint

from .models import Product
from .forms import ProductCreateForm, CouponCreateForm
from .scripts.ScrapeAmazon import AmazonScraper
from .scripts.helper import *
# Create your views here.

def product_home_view(request):
	return HttpResponse('<h1>Home</h1>')

def product_create_view(request):
	product_form = ProductCreateForm(request.POST or None)
	coupon_form = CouponCreateForm(request.POST or None)

	context = {}
	if product_form.is_valid() and coupon_form.is_valid():
		amazon_url = request.POST.get('amazon_url')
		amazon = AmazonScraper(amazon_url)
		json = amazon.get_json()
		pprint(json)

		coupon = coupon_form.save()
		json.update({
			'amazon_url': amazon_url,
			'slug': slugify(random_string()),
			'coupon': coupon,
		})

		images = json.pop('images')

		product = Product(**json)
		product.save()

		for image in images:
			l = image.get('large')
			s = image.get('small')
			product.pictures.create(small_picture = s, large_picture = l)

		product_form = ProductCreateForm()
		coupon_form = CouponCreateForm()
		context['generated_url'] = product.get_absolute_url()

	context['product_form'] = product_form
	context['coupon_form'] = coupon_form
	return render(request, 'product_create.html', context)

def product_details_view(request, slug):
	return render(request, 'product_details.html', {})


class ProductDetailView(DetailView):
	template_name = 'product_details.html'
	queryset = Product.objects.all()
