import unittest
from UnitestFrame.class_one import A
from UnitestFrame.class_two import B

if __name__ == '__main__':
    print("This is main class")
    suite1 = unittest.TestLoader().loadTestsFromTestCase(A)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(B)
    t = [suite1, suite2]
    main_suite = unittest.TestSuite(t)
                or 
    main_suite = unittest.TestSuite()
    main_suite.addTest(A('test_001'))

    unittest.TextTestRunner().run(main_suite)
