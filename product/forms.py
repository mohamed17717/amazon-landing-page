from django import forms

from .models import Product, Coupon

class ProductCreateForm(forms.ModelForm):
	amazon_url = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={
			'placeholder': 'Amazon product URL',
			'type': 'url',
			'autocomplete': 'off'
		})
	)

	# forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder': 'Title',}))
	class Meta:
		model = Product
		fields = ('amazon_url',)

	def clean_amazon_url(self):
		amazon_url = self.cleaned_data.get('amazon_url')
		if not amazon_url.startswith('https://www.amazon.com/'):
			raise forms.ValidationError('url must be on amazon')
		return amazon_url

class CouponCreateForm(forms.ModelForm):
	code = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={
			'placeholder': 'Coupon Code',
			'type': 'text',
			'autocomplete': 'off'
		})
	)
	howlong = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={
			'placeholder': 'Howlong Coupon remian?',
			'type': 'number',
			'autocomplete': 'off'
		})
	)
	howmany = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={
			'placeholder': 'Howmany Coupons?',
			'type': 'number',
			'autocomplete': 'off'
		})
	)
	salepercent = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={
			'placeholder': 'Sale %',
			'type': 'number',
			'autocomplete': 'off'
		})
	)
	class Meta:
		model = Coupon
		fields = (
			'code',
			'howlong',
			'howmany',
			'salepercent',
		)
