import unittest
from time import sleep
from selenium import webdriver

class BaseTestClass(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(120)
        self.driver.get("https://www.amazon.in")
        self.driver.maximize_window()
        return self.driver

    def tearDownClass(self):
        sleep(5)
        self.driver.close()
