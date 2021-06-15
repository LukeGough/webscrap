# Import the beautifulsoup4 library
from bs4 import BeautifulSoup

# Access the content in the home.html file
	# Will be using file objects
	# html_file is the variable
with open('home.html','r') as html_file:
	content = html_file.read()
	#print(content)

	soup = BeautifulSoup(content, 'lxml')
	# second parameter will let you filter
		# need to use _ before class as class is a builtin python keyword
	course_cards = soup.find_all('div', class_='card')
	for course in course_cards:
		course_name = course.h5.text
		course_price = course.a.text.split()[-1]
		print(f'{course_name} costs {course_price}')
