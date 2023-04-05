from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login_Logout
from utilities.readProperties import Read_Config
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl = Read_Config.getApplicationUrl()
    username = Read_Config.getUsername()
    password = Read_Config.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepageTitle(self,setup):
        self.logger.info("******************Test_001_Login****************")
        self.logger.info("******************Verifying Home Page Title****************")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_Title = self.driver.title
        self.driver.close()
        if act_Title == "Your store. Login":
            assert True
            self.logger.info("*****************Home Page title test is passed****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            assert False
            self.logger.error("*****************Home Page Title test is FAILED****************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("****************Login Test started****************")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login_Logout(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        login_title = self.driver.title
        self.driver.close()
        if login_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******************Login Test Passed****************")

        else:
            #self.driver.save_screenshot('./Screenshots/'+'test_login.png')
            #self.driver.get_screenshot_as_file('test_login.png')
            self.driver.close()
            assert False
            self.logger.error("***************Login Test failed****************")



# pytest -v -s --capture=tee-sys --html=Reports/report.html testCases/test_login.py