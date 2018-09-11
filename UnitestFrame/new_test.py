import unittest

class new_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup class")

    def test_A(self):
        print("function a")

    def test_B(self):
        print("function b")

    def test_C(self):
        print("function c")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")


if __name__ == '__main__':
    unittest.main()