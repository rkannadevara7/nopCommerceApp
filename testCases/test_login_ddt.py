import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\LoginData.xlsx"
    log = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.log.info("**********Test_002_DDT_Login****************")
        self.log.info("************Verifying Login DDT test*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path,'Sheet1')
        print("No. of rows in excel file are: ", self.rows)
        lst_status = []
        for r in range(2,self.rows+1):
            self.user = ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if actual_title == exp_title:
                if self.exp == "Pass":
                    self.log.info("********passed*************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.log.info("**********Failed***********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif actual_title!=exp_title:
                if self.exp == "Pass":
                    self.log.info("********Failed*************")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.log.info("**********Passed***********")
                    lst_status.append("Pass")

        if 'Fail' not in lst_status:
            self.log.info("*********Login DDT Test is passed**********")
            self.driver.close()
            assert True
        else:
            self.log.info("*********Login DDT Test is failed**********")
            self.driver.close()
            assert False

        self.log.info("*********End of Login DDT Test**********")
        self.log.info("*********Completed Test_002_DDT_Login test case**********")
