"""
Basic example of selenium+beautifulsoup web-scraping
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from pprint import pprint
import time

url = 'https://www.seasonalfoodguide.org/'

browser = webdriver.Chrome()
browser.get(url)
states = Select(browser.find_element_by_id('sfg-state'))
time.sleep(3.0)
states.select_by_visible_text('Nevada')

season = Select(browser.find_element_by_id('veg-calendar'))
time.sleep(1.0)
season.select_by_visible_text('Late December')

html = browser.page_source
pprint(html)

soup = BeautifulSoup(html, 'lxml')
veggies = soup.findAll('h3', {'class': 'card-title'})
pprint(veggies)
for veggie in veggies:
    pprint(veggie.getText())


browser.quit()