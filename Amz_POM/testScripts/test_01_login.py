from Amz_POM.common.basetest import BaseTestClass
from Amz_POM.pageObject.page_actions import PageActionsClass

class test_01_login(BaseTestClass):

    pg_act = PageActionsClass()
    PageActionsClass.login_action(pg_act)


