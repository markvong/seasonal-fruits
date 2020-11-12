"""
Web-scrape tool utilizing Selenium and BeautifulSoup4
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
from pprint import pprint
import time
import json
import os
url         = 'https://www.seasonalfoodguide.org/'
config_file = 'config.json'
save_file   = 'fruit_list.json'
fruit_folder = 'fruit_images/'
load_delay = 3.0
scrape_delay = 1.0

state_retrieval = False
fruit_retrieval = True
save_data       = False

def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def open_config():
    with open(config_file, 'r') as infile:
        configs = json.load(infile)
    print(configs)
    return configs

def retrieve_data():
    if is_non_zero_file(save_file):
        with open(save_file, 'r') as infile:
            data = json.load(infile)
        return data
    else:
        return {}

"""
Find way to segment file write on each month
"""
def main():
    data = retrieve_data()
    configs = open_config()
    browser = webdriver.Chrome(ChromeDriverManager().install()) # set up selenium browser and automatically installs the correct chrome driver
    browser.get(url) # opens up browser and goes to specified url
    if state_retrieval:
        for state in configs['states']:
            if state not in data:
                data[state] = {}
                try:
                    select = Select(browser.find_element_by_id('sfg-state'))
                except Exception as e:
                    print('Error occurred in parsing: {:s}'.format(e))
                    browser.quit()
                    return
                
                select.select_by_visible_text(state)
                for month in configs['months']:
                    for prefix in configs['period_prefix']:
                        season = '{:s} {:s}'.format(prefix, month)
                        data[state][season] = []

                        calendar = Select(browser.find_element_by_id('veg-calendar'))
                        time.sleep(load_delay)
                        calendar.select_by_visible_text(season)
                        time.sleep(scrape_delay)

                        html = browser.page_source
                        soup = BeautifulSoup(html, 'lxml')
                        produce_list = soup.findAll('h3', {'class': 'card-title'})
                        
                        for produce in produce_list:
                            data[state][season].append(produce.getText())
                    with open(save_file, 'w') as infile:
                        json.dump(data, infile)
    elif fruit_retrieval: # this is my fruit data retrieval
        html = browser.page_source # get the html from the opened website
        soup = BeautifulSoup(html, 'lxml') # convert it into beautiful soup, you're beautiful
        fruit_card = soup.findAll('div', {'class': 'card-body'}) # finds all divs w/ specified class
        for fruit_card_tag in fruit_card:
            fruit_name = fruit_card_tag.a['href'].strip('/').split('/')[1].replace('-', ' ')
            fruit_desc = fruit_card_tag.getText()
            data[fruit_name] = fruit_desc
        fruit_imgs = soup.findAll('img', {'class': 'card-image1'}) # finds all imgs w/ specified class
        for fruit_img_tag in fruit_imgs:
            
            fruit_url = '{:s}{:s}'.format(url, fruit_img_tag['src']) # get specified url of image
            req = Request(fruit_url, headers={'User-Agent': 'Mozilla/5.0'}) # create new request object (this is stack overlfow)
            webpage = urlopen(req).read() # stack overflow but it reads the image in bytes i think

            fruit_name = '_'.join(fruit_img_tag['alt'].split('-')[1:])
            fruit_img_filepath = '{:s}{:s}.jpg'.format(fruit_folder, fruit_name)
            with open(fruit_img_filepath, 'wb') as infile:
                infile.write(webpage)

    if save_data:
        pprint(data)
        with open(save_file, 'w') as infile:
            json.dump(data, infile)
        pprint('Saved data to {:s}'.format(save_file))

    browser.quit()

if __name__ == "__main__":
    main()
