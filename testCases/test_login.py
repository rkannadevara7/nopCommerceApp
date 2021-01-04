import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    log = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.log.info("************Test_001_Login*************")
        self.log.info("************Verify home page title*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.log.info("************Home page title test is passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.log.info("************Home page title test is failed*************")
            assert  False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.log.info("************Verifying Login test*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.log.info("************Login test is passed*************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.log.info("************Login test is failed*************")
            assert False
