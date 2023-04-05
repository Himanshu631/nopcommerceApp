import random
import string

import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login_Logout
from pageObjects.AddCustomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import Read_Config


class Test003_AddCustomer:
    baseurl = Read_Config.getApplicationUrl()
    username = Read_Config.getUsername()
    passwd = Read_Config.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("*******Test_003_Add_Customer********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login_Logout(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.passwd)
        self.lp.clickLogin()
        self.logger.info("********Login Successful**********")

        self.logger.info("********Starting Add Customer Test*********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustmenu()
        self.addcust.clickoncustsubmenu()

        self.addcust.clickaddnew()

        self.logger.info("*********Providing Customer Info*********")

        self.email = random_generator()+"@gmail.com"
        self.addcust.addemail(self.email)
        self.addcust.addpassword("test123re")
        self.addcust.addfname("Arvind")
        self.addcust.addlname("Singh")
        self.addcust.addgender("Male")
        self.addcust.adddob("4/26/1983")
        # self.addcust.setcustrole("Vendors")
        self.addcust.clicksave()

        self.logger.info("*******Saving Customer Info********")
        self.logger.info("*******Add Customer Validation Started********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "The new customer has been added successfully" in self.msg:
            assert True
            self.logger.info("******Add Customer Passed******")

        else:
            self.logger.error("*********Add Customer Failed**********")
            assert False

        self.driver.close()
        self.logger.info("*******Ending Test_003_Add_Customer Test*********")


def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars)for x in range(size))
