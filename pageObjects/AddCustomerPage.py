from selenium.webdriver.common.by import By


class AddCustomer:
    lnk_customers = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_customers_submenu_xpath = "//a[@href='/Admin/Customer/List']"
    btn_add_new = "//a[@class='btn btn-primary']"

    cust_email = "//input[@id='Email']"
    cust_passwd = "//input[@id='Password']"
    cust_first_name = "//input[@id='FirstName']"
    cust_last_name = "//input[@id='LastName']"

    radio_male = "//input[@id='Gender_Male']"
    radio_female = "//input[@id='Gender_Female']"

    cust_dob = "//input[@id='DateOfBirth']"
    cust_company = "//input[@id='Company']"

    cust_role = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    cust_roles_administrator = "//li[contains(text(),'Administrators')]"
    cust_roles_forum_mod = "//li[contains(text(),'Forum Moderators')]"
    cust_roles_guest = "//li[contains(text(),'Guests')]"
    cust_roles_registr = "//li[contains(text(),'Registered')]"
    cust_roles_vendor = "//li[contains(text(),'Guests')]"

    cust_checkbox = "//input[@id='Active']"

    cust_save = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickoncustmenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customers).click()

    def clickoncustsubmenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_submenu_xpath).click()

    def clickaddnew(self):
        self.driver.find_element(By.XPATH, self.btn_add_new).click()

    def addemail(self, email):
        self.driver.find_element(By.XPATH, self.cust_email).send_keys(email)

    def addpassword(self, password):
        self.driver.find_element(By.XPATH, self.cust_passwd).send_keys(password)

    def addfname(self, fname):
        self.driver.find_element(By.XPATH, self.cust_first_name).send_keys(fname)

    def addlname(self, lname):
        self.driver.find_element(By.XPATH, self.cust_last_name).send_keys(lname)

    def adddob(self, dob):
        self.driver.find_element(By.XPATH, self.cust_dob).send_keys(dob)

    def addCompany(self, company):
        self.driver.find_element(By.XPATH, self.cust_company).send_keys(company)

    def addgender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.radio_male).click()

        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.radio_female).click()

        else:
            self.driver.find_element(By.XPATH, self.radio_male).click()


    def setcustrole(self, crole):
        self.driver.find_element(By.XPATH, self.cust_role).click()
        if crole == "Registered":
            self.litem = self.driver.find_element(By.XPATH, self.cust_roles_registr)

        elif crole == "Forum Moderators":
            self.litem  = self.driver.find_element(By.XPATH, self.cust_roles_registr)

        elif crole == "Administrators":
            self.litem  = self.driver.find_element(By.XPATH, self.cust_roles_administrator)

        elif crole == "Vendors":
            self.litem  = self.driver.find_element(By.XPATH, self.cust_roles_vendor)

        elif crole == "Guests":
            self.driver.find_element(By.XPATH, "//span[@class='k-icon k-i-close']")
            self.litem  = self.driver.find_element(By.XPATH, self.cust_roles_guest)

        else:
            self.driver.find_element(By.XPATH, "//div[@class='input-group-append input-group-required']//div[@role='listbox']").clear()
            self.litem = self.driver.find_element(By.XPATH, self.cust_roles_guest)

        self.driver.execute_script("arguments[0].click();", self.litem)

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.cust_save).click()

