import pytest
import time

from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    log = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.log.info("************Test_003_AddCustomer*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("*************Login Successful*********")

        self.log.info("*************Starting Add Customer test********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(2)
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNew()

        self.log.info("***********Providing customer info************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Rama")
        self.addcust.setLastname("Krishna")
        self.addcust.setGender("Male")
        self.addcust.setDob("01/07/1991")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setVendors("Vendor 2")
        self.addcust.setAdminComment("This is for testing")
        self.addcust.clickOnSave()

        self.log.info("**********Saving Customer Info**********")

        self.log.info("**********Add Customer Validation Started*********")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.log.info("******Add Customer test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.log.error("********Add Customer test failed ***********")
            assert True == False

        self.driver.close()
        self.log.info("*******Ending Add Customer test case ************")


def random_generator(size=8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
