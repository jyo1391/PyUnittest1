import unittest
from time import sleep

from selenium import webdriver


class ExClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.amazon.com')

    def test_case_1(self):
        print("This is test case 1")

    def test_case_2(self):
        print("This is test case 2")

    def test_case_3(self):
        print("This is test case 3")

    def tearDown(self):
        sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
