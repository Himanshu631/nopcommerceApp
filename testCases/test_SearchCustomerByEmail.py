import time

import pytest

from pageObjects.LoginPage import Login_Logout
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import Read_Config
from utilities.customLogger import LogGen


class Test004_SearchCustomerByEmail:
    baseurl = Read_Config.getApplicationUrl()
    username = Read_Config.getUsername()
    password = Read_Config.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("**********SearchCustomerByEmail**********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login_Logout(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("**********Login Successful**********")

        self.logger.info("**********Starting search customer by email**********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustmenu()
        self.addcust.clickoncustsubmenu()

        self.logger.info("**********Seachig customer By Email Id**********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()

        time.sleep(5)

        status = searchcust.SearchCustomersByEmail("victoria_victoria@nopCommerce.com")
        assert True == status

        self.driver.close()
        self.logger.info("**********Test 004 SearchCustomer By Email Completed**********")
