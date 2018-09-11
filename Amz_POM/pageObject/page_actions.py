from Amz_POM.pageObject.elements import ElementsClass

class PageActionsClass(ElementsClass):


    def login_action(self):
        ec = ElementsClass()
        try:
            ec.signin.click()
            #ec.emailAddress.send_keys('jyothi1391@gmail.com')
        except Exception as e:
            print(e.__class__)

        '''
        ec.emailCont.click()
        ec.passwd.send_keys('123jyothi123')
        ec.loginBtn.click()
        '''




