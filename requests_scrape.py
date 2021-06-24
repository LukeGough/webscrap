# Import the beautifulsoup4 library
from bs4 import BeautifulSoup
import requests
import re
from urllib.request import Request, urlopen

req = Request('http://www.cmegroup.com/trading/products/#sortFi', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
print(webpage)
#html_text = requests.get('http://www.bom.gov.au/wa/forecasts/perth.shtml').text
#html_text = requests.get('http://www.bom.gov.au/wa/forecasts/perth.shtml')
#print(html_text)
#soup = BeautifulSoup(html_text, 'lxml')
	#https://www.youtube.com/watch?v=XVv6mJpFOb0
	#30:00
#days = soup.find_all('div', class_ = 'day')
#days = soup.find_all('div', {'class' : re.compile('day*')})
#print(days)

