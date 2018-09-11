import unittest

class A(unittest.TestCase):


    def setUp(self):
        print("open broswer")

    def test_001(self):
        print("Test case 1 from class A")

    def test_002(self):
        print("Test case 2 from class A")

    def tearDown(self):
        print("close browser")