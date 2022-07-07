from bs4 import BeautifulSoup
import requests
import lxml

# This is the URL of the site you want to scrap
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
#Pulls HTML data from the URL
page = requests.get(url)   
#Cleans up the HTML so it is readable
soup = BeautifulSoup(page.text, 'lxml')

print(soup)