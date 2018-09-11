from Amz_POM.common.basetest import BaseTestClass
from time import sleep
class ElementsClass(BaseTestClass):

    b_tst = BaseTestClass()
    driver = b_tst.setUp()
    signin = driver.find_element_by_xpath('//a[@id="nav-link-yourAccount"]')
    sleep(5)
    #emailAddress = driver.find_element_by_xpath('//input[@type="email"]')
    '''
    emailCont = driver.find_element_by_xpath('//input[@id="continue"]')
    passwd = driver.find_element_by_xpath('//input[@id="ap_password"]')
    loginBtn = driver.find_element_by_xpath('//input[@id="signInSubmit"]')
    '''