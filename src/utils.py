from pygooglenews import GoogleNews as GN

class GoogleNews():
	def __init__(self, lang:str='en', country:str='US'):
		self.GN = GN(lang=lang,country=country)
	def search(self, query:str, helper=True, when=None, from_=None, to_=None, proxies=None, scraping_bee=None):
		if when:
			return self.GN.search(query=query, helper=helper, when=when,proxies=proxies, scraping_bee=scraping_bee)
		if from_ and not when:
			query = query + ' after:' + from_
		if to_ and not when:
			query = query + ' before:' + to_
		return self.GN.search(query=query, when=when, proxies=proxies, scraping_bee=scraping_bee)
