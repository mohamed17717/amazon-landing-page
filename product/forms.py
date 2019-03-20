from django import forms

from .models import Product, Coupon

class ProductCreateForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('amazon_url',)

	def clean_amazon_url(self):
		amazon_url = self.cleaned_data.get('amazon_url')
		if not amazon_url.startswith('https://www.amazon.com/'):
			raise forms.ValidationError('url must be on amazon')
		return amazon_url

class CouponCreateForm(forms.ModelForm):
	class Meta:
		model = Coupon
		fields = (
			'code',
			'howlong',
			'howmany',
			'salepercent',
		)
