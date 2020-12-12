from threading import Thread
from lxml import html
from review import review, review_source
import time
import requests

def extract(url: str):
	timer_sleep = 10
	current_str = ""
	try:
		time.sleep(timer_sleep)

		r = requests.get(url)
		
		tree = html.fromstring(r.text)
		
		current_str = ""
		for p in tree.xpath('//p/text()'):
			current_str = current_str + p

		return current_str
	except:
		return current_str

def parse_web_irec():
	extra_news = 19
	urls = [r"https://irecommend.ru/content/rzhd",
		    'https://irecommend.ru/content/rzhd?page=1', 
		    'https://irecommend.ru/content/rzhd?page=2', 
		    'https://irecommend.ru/content/rzhd?page=3', 
		    'https://irecommend.ru/content/rzhd?page=4',
		    'https://irecommend.ru/content/rzhd?page=5']

	for url in urls:
		r = requests.get(url)
		
		tree = html.fromstring(r.text)
	
		comments = tree.xpath('//a[starts-with(@class,"more")]/@href')

		texts_list = []
		reviews_list = []
		for ind in range(len(comments) - extra_news):
			comment = comments[ind]
			newUrl = 'https://irecommend.ru' + comment
			text = extract(newUrl)
			if len(text) > 10:
				texts_list.append(text)
				
				r = review()
				r.url = newUrl
				r.text = text
				r.source = 1
				reviews_list.append(r)

		return (reviews_list, texts_list)
