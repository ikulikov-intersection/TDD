##definition
from selenium import webdriver
import unittest
browser = webdriver.Firefox()

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')












##starting do somthing
browser.get("http://localhost:8000")
assert 'To-Do' in browser.title, "browser title was" + browser.title

webdriver.firefox


##


##
