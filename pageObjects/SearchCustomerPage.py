from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_email = "//input[@id='SearchEmail']"
    txt_fname = "//input[@id='SearchFirstName']"
    txt_lname = "//input[@id='SearchLastName']"
    btn_Search = "//button[@id='search-customers']"

    table_xpath = "//table[@id='customers-grid']"
    trows = "//table[@id='customers-grid']//tbody/tr"
    tcols = "//table[@id='customers-grid']//tbody/tr/td"
    
    def __init__(self,driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email).clear()
        self.driver.find_element(By.XPATH,self.txt_email).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txt_fname).clear()
        self.driver.find_element(By.XPATH,self.txt_fname).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element(By.XPATH, self.txt_lname).clear()
        self.driver.find_element(By.XPATH,self.txt_lname).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btn_Search).click()

    #def getNoofRows(self):  #wrong
    #    return len(self.driver.find_element(By.XPATH,self.trows))

    #def getNoofCols(self):  #wrong
    #    return len(self.driver.find_element(By.XPATH, self.tcols))

    def SearchCustomersByEmail(self,email):
        flag  = False
        for r in range(1,2):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def SearchCustomersByName(self, Name):
        flag  = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
