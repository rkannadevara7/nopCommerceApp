import time
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    log = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.log.info("************Test_005_SearchCustomerByName*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("**************Login Successful****************")

        self.log.info("***************Navigating to Search Customer page****************")

        addcust = AddCustomer(self.driver)
        addcust.clickOnCustomersMenu()
        time.sleep(2)
        addcust.clickOnCustomersMenuItem()

        self.log.info("***********Starting Search Customer by Name***************")

        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status

        self.log.info("*********TC_Test_005_SearchCustomerByName is finished************")

        self.driver.close()
