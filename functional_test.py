##definition
from selenium import webdriver
browser = webdriver.Firefox()


##starting do somthing
browser.get("http://localhost:8000")
assert 'Django' in browser.title
webdriver.firefox


##


##
