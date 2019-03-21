from .scraper import Scraper

from re import findall, sub
from pprint import pprint
from urllib.parse import unquote

class AmazonScraper(object):
	"""docstring for AmazonScraper
		scrape specific data about the product from 
		amazon
	"""

	def __init__(self, productLink):
		super(AmazonScraper, self).__init__()

		self.productLink = productLink
		self.scraper = Scraper()

		# start work
		cookies = self.scraper.get_cookies('firefox', 'amazon.com')
		self.scraper.set_cookies(cookies)
		self.scraper.get(self.productLink)
		self.scraper.html_soup()

	def get_product_images(self):
		ptrn = r'https:[\w\.\%\/-]+\.jpg'
		# urls = findall(ptrn, self.scraper.src)
		urls = self.scraper.soup.select('#altImages img')
		print('1', urls)
		urls = [elm.get('src') for elm in urls]
		urls = [url for url in urls if url.endswith('.jpg')]
		print('2', urls)

		small_images = urls
		print('4', small_images)
		# ptrn = r'\._[A-Z]{2}40_\.jpg$'
		
		# for url in urls:
		# 	end = findall(ptrn, url)
		# 	if not end: 
		# 		break
			# small_images.append(url)
		
		images = []
		# ptrn = r'\._[A-Z]{2}40_'
		ptrn = r'\._.+_'
		[images.append({
			'small': i, 
			'large': sub(ptrn, '', i),
		}) for i in small_images]
		print('3', images)
		return images

	def get_product_title(self):
		soup = self.scraper.soup
		title = None
		elm = soup.select_one('meta[name="title"]')
		if elm:
			title = unquote(elm.get('content'))
		return title

	def get_product_price(self):
		soup = self.scraper.soup
		elm = soup.select_one('#price')
		elm.style and elm.style.decompose()
		if elm:
			elmContent = [i.strip() for i in elm.text.split('\n') if i]
			try:
				priceIndex = elmContent.index('Price:')
				priceNumber = findall(r'[\d\.]+', elmContent[priceIndex+1])
				priceNumber = max([float(num) for num in priceNumber])
				return priceNumber # elmContent[priceIndex+1].strip('$').replace(',', '')
			except ValueError:
				return ''

	def get_product_description(self):
		soup = self.scraper.soup
		# elm = soup.select_one('#productDescription_feature_div p')
		# if elm:
		# 	return elm.html
		# else:
		elms = soup.select('#feature-bullets li > span')
		return '\n'.join([elm.text.strip() for elm in elms if not elm.a])
	
	def get_json(self):
		return {
			'images': self.get_product_images(),
			'title': self.get_product_title(),
			'price': self.get_product_price(),
			'description': self.get_product_description(),
		}
	


if __name__ == '__main__':

	# url = 'https://www.amazon.com/Samsung-Chromebook-XE500C13-K04US-Certified-Refurbished/dp/B0759YSF4W/ref=br_asw_pdt-2?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=EGXH0KTHXRHA05NCHX24&pf_rd_t=36701&pf_rd_p=f05a98e0-3eaa-471e-b2f1-f6d8d5a04287&pf_rd_i=desktop'
	# url = 'https://www.amazon.com/dp/B07L2X16J4/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07L2X16J4&pd_rd_w=oPyUD&pf_rd_p=80559f3c-f83b-49c1-8a72-40f936e9df7a&pd_rd_wg=3IXF5&pf_rd_r=2BF8BJX24G92HM6MJ7C5&pd_rd_r=039436b6-49f9-11e9-af43-e53d38e7cbfa'
	# url = 'https://www.amazon.com/dp/B07D8KCZ31/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07D8KCZ31&pd_rd_w=sbzil&pf_rd_p=80559f3c-f83b-49c1-8a72-40f936e9df7a&pd_rd_wg=yrx4u&pf_rd_r=73SJHN9NJM5458B2KMA0&pd_rd_r=40621fcf-4a67-11e9-9cb1-0dad9803f47d'
	url = 'https://www.amazon.com/Invicta-1270-Specialty-Chronograph-Ion-Plated/dp/B005D3YMKI/ref=br_asw_pdt-6?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=13XRJCH7BZE8SJQM35Z9&pf_rd_t=36701&pf_rd_p=bd8d012b-e231-468e-a365-e42e25a5b501&pf_rd_i=desktop&fbclid=IwAR1T33ZHh3qtzUgJUmdZbHii8SumByS4lVgO91ir88paGDKa1VIb25YskKI'
	a = AmazonScraper(url)

	pprint(
		a.get_json()
	)



