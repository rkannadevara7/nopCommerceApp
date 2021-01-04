import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menu_item_xpath="//span[@class='menu-item-title'][text()='Customers']"
    btnAddnew_xpath="//a[@class ='btn bg-blue']"
    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_id="FirstName"
    txtLastName_id="LastName"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtDob_id="DateOfBirth"
    txtCompanyname_id="Company"
    cbTaxExempt_id="IsTaxExempt"
    txtNewsletter_xpath="//div[@class ='k-multiselect-wrap k-floatwrap']"
    lstitemYourStore_xpath="//li[contains(text(),'Your store name')]"
    lstitemTestStore_xpath = "//li[contains(text(),'Test store 2')]"
    #txtcustomerRoles_xpath="//div[@class='form-group'][@xpath=1]//div[@class ='k-multiselect-wrap k-floatwrap']"
    txtcustomerRoles_xpath = "//body/div[3]/div[3]/div[1]/form[1]/div[3]/div[1]/nop-panels[1]/nop-panel[1]/div[1]/div[2]/div[1]/div[10]"
    lstitemAdministrators_xpath="//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpMgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_id="AdminComment"
    btnSave_xpath="//button[@name='save']"
    btnSaveAndcontinue_xpath = "//button[@name='save-continue']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_item_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setFirstname(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element(By.ID, self.txtDob_id).send_keys(dob)

    def setCompanyName(self, compname):
        self.driver.find_element(By.ID, self.txtCompanyname_id).send_keys(compname)

    def setTaxExemptId(self):
        self.driver.find_element(By.ID, self.cbTaxExempt_id).click()

    def setNewsLetter(self, value):
        self.driver.find_element(By.XPATH, self.txtNewsletter_xpath).click()
        time.sleep(3)
        if value == 'Your Store Name':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemYourStore_xpath)
        elif value == 'Test Store 2':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemTestStore_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemYourStore_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setVendors(self, value):
        drp = Select(self.driver.find_element(By.XPATH,self.drpMgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self, comment):
        self.driver.find_element(By.ID, self.txtAdminComment_id).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    def clickOnSaveAndContinue(self):
        self.driver.find_element(By.XPATH, self.btnSaveAndcontinue_xpath).click()





