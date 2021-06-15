# Import the beautifulsoup4 library
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.seek.com.au/python-jobs').text
soup = BeautifulSoup(html_text, 'lxml')
	#https://www.youtube.com/watch?v=XVv6mJpFOb0
	#30:00
