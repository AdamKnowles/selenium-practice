from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def search(str):

    browser = webdriver.Chrome(r"C:\Users\ackno\workspace\selenium\driver\chromedriver.exe")

    
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



  


