import requests 
from bs4 import BeautifulSoup

class Celebrity:
	"""
		Signature : Celebrity(self, name, img_src, details)
		@parms name    : Name of the celebrity 
		@parms img_src : source of the image
		@parms details : details of the celebrity

		This class store the information about the celebrity
	"""
	def __init__(self, name, img_src, details):
		self.name = name
		self.img_src = img_src
		self.details = details

	def __str__(self):
		"""
		Signature : __str__(self)
		This function will be called automatically when object of Celebrity class is pass in print
		"""

		return "Name\t:\t" + self.name + "\nImage\t:\t" + self.img_src + "\nDetails\t:\t" + self.details

def get_name(list_item):
	"""
		Signature : get_name(list_item)
		This function fetch the name of the celebrity
		@parms list_item : html content 
	"""
	name = list_item.find("h3",attrs = {"class":"lister-item-header"}).text
	name = name.strip()
	name = "".join(name.split("\n")[1:])
	name = name.strip()
	return name
	
def get_details(list_item):
	"""
		Signature : get_details(list_item)
		This function fetch the details of the celebrity
		@parms list_item : html content 
	"""	
	details = list_item.findAll("p")[-1].text
	details = details.strip()
	return details

def get_image(list_item):
	"""
		Signature : get_image(list_item)
		This function fetch the image source of the celebrity's image
		@parms list_item : html content 
	"""
	img_src = list_item.find("img")["src"]
	img_src = img_src.strip()
	return img_src

URL = "http://m.imdb.com/feature/bornondate"  # url from where we are scraping the data

request = requests.get(URL) # fetching the data from the url

html_code = BeautifulSoup(request.content, "html5lib") # converting the data into html format

list_items = html_code.findAll("div", attrs = {"class":"lister-item mode-detail"}) # targeting the required section of the html code

celebrities_list = list()

for list_item in list_items: # iterating the list 
	name = get_name(list_item) # fetching the name
	details = get_details(list_item) # fetching details of the celebrity
	img_src = get_image(list_item) # Saving source of the celebrity's image
	celebrity = Celebrity(name, img_src, details) #creating object of the celebrity
	celebrities_list.append(celebrity)
	

for index in range(6):
	print(celebrities_list[index])
	print("="*140)