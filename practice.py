from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from secrets import secrets


def search(str):
    
    # secrets is the variable for the chrome webdriver path
    browser = secrets

    
    browser.get('http://google.com/')
    search_input = browser.find_element_by_name('q')
    time.sleep(1)
    search_input.send_keys(str)
    time.sleep(1)
    search_input.send_keys(Keys.RETURN)
    time.sleep(1)
    browser.find_element_by_class_name('r').click()
    time.sleep(8)

    

search("Adam Knowles Nashville")



  


