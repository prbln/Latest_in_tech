import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(res.text,'html.parser')
item = soup.select('.morelink')
res2 = requests.get('https://news.ycombinator.com/'+item[0].get('href'))

hn = []
def get_info(response):
	res = response
	soup = BeautifulSoup(res.text,'html.parser')
	votes = soup.select('.score')
	links = soup.select('.storylink')

	def create_custom_hn(links,votes):
		
		for ind,item in enumerate(links):
			title = item.getText()
			href = item.get('href', None)
			vote = (votes[ind].string).split(' ')
			
			if int(vote[0]) > 100:
				hn.append({'title': title , 'link': href , 'points':int(vote[0])})
		return hn
	return create_custom_hn(links,votes)
get_info(res2)
pprint.pprint(sorted(get_info(res),key = lambda x:x['points'],reverse = True))
'''
I want to build upon this by outputing it on a website so that I can directly access
the links.
extend beyond terminal
''' 

