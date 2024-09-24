from selenium.webdriver.common.by import By
class OrangeLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.forgot_password = (By.XPATH, '//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]')
        self.username_input = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
        self.reset_password = (By.XPATH,'//button[@class="oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset"]')

####Header validation
        self.username_input = (By.XPATH, '//input[@placeholder="Username"]')
        self.password_input = (By.XPATH, '//input[@placeholder="Password"]')
        self.login_submit = (By.XPATH, '//button[@type="submit"]')
        # Page Title Validation:
        def title_validation():
            given_title = "OrangeHRM"
            page_title = (driver.title)
            if given_title == page_title:
                print("Title validated sucessfully")
            else:
                print("Not a valid title")
        title_validation()

#header locators
        self.adminpg_h1 = (By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
        self.adminpg_h2 = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
        self.adminpg_h3 = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
        self.adminpg_h4 = (By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
        self.adminpg_h5 = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a')
        self.adminpg_h6 = (By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a')
        self.adminpg_h7 = (By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span')
#menu locators
        self.menu_opt1 = (By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
        self.menu_opt2 = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
        self.menu_opt3 = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span')
        self.menu_opt4 = (By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span')
        self.menu_opt5 = (By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span')
        self.menu_opt6 = (By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span')
        self.menu_opt7 = (By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span')
        self.menu_opt8 = (By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span')
        self.menu_opt9 = (By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span')
        self.menu_opt10 = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a')
        self.menu_opt11 = (By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span')

    def click_forgot_password(self):
        self.driver.find_element(*self.forgot_password).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def click_reset_password(self):
        self.driver.find_element(*self.reset_password).click()

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_submit(self):
        self.driver.find_element(*self.login_submit).click()

    def header_validation(self):
        h1 = self.driver.find_element(*self.adminpg_h1.text)
        h2 = self.driver.find_element(*self.adminpg_h2.text)
        h3 = self.driver.find_element(*self.adminpg_h3.text)
        h4 = self.driver.find_element(*self.adminpg_h4.text)
        h5 = self.driver.find_element(*self.adminpg_h5.text)
        h6 = self.driver.find_element(*self.adminpg_h6.text)
        h7 = self.driver.find_element(*self.adminpg_h7.text)
    def menu_validation(self):
        m1 = self.driver.find_element(*self.menu_opt1.text)
        m2 = self.driver.find_element(*self.menu_opt2.text)
        m3 = self.driver.find_element(*self.menu_opt3.text)
        m4 = self.driver.find_element(*self.menu_opt4.text)
        m5 = self.driver.find_element(*self.menu_opt5.text)
        m6 = self.driver.find_element(*self.menu_opt6.text)
        m7 = self.driver.find_element(*self.menu_opt7.text)
        m8 = self.driver.find_element(*self.menu_opt8.text)
        m9 = self.driver.find_element(*self.menu_opt9.text)
        m10 = self.driver.find_element(*self.menu_opt10.text)
        m11 = self.driver.find_element(*self.menu_opt11.text)

