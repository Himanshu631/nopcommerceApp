import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login_Logout
from utilities.readProperties import Read_Config
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:  # data drive testcase
    baseurl = Read_Config.getApplicationUrl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("****************Test 002 DDT Login")
        self.logger.info("****************Login Test started****************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login_Logout(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows in Excel", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            self.driver.maximize_window()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Passed******")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed*******")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Failed******")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("******Passed******")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("*********End of login DDT*******")
        self.logger.info("*********Completed TClogin002 DDT*******")

# pytest -v -s --capture=tee-sys --html=Reports/report.html testCases/test_login.py
