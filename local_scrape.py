# Import the beautifulsoup4 library
from bs4 import BeautifulSoup

# Access the content in the home.html file
	# Will be using file objects
	# html_file is the variable
with open('home.html','r') as html_file:
	content = html_file.read()
	#print(content)

	soup = BeautifulSoup(content, 'lxml')
	courses_html_tags = soup.find_all('h5')
	for course in courses_html_tags:
		print(course.text)
