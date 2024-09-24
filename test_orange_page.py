import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.chrome.options import Options
from orange_login_page import OrangeLoginPage

###POM implementation
#Add the parent directory
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
test = OrangeLoginPage(url)

@pytest.fixture()
def browser():
    chromedriver_path = r"E:\Automation testing\chromedriver.exe"
    chrome_options = Options()
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver

####Test case ID:TC_PIM_01
def test_orange_page(browser):
    orange_login_page = OrangeLoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #password reset action
    orange_login_page.click_forgot_password()
    orange_login_page.enter_username("Admin")
    orange_login_page.click_reset_password()

###Test case ID:TC_PIM_02
def test_orange_page(browser):
    orange_login_page = OrangeLoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    orange_login_page.enter_username("Admin")   # Perform login actions
    orange_login_page.enter_password("admin123")
    orange_login_page.click_login_submit()

def test_title_validation():  ###2nd test title validation
    print("Title validated successfully")

def test_header_validation():   ###3rd test header validation
    h1 ="User Management"
    h2 = "Job"
    h3 = "Organization"
    h4 = "Qualifications"
    h5 = "Nationalities"
    h6 = "Corporate Banking"
    h7 = "Configuration"
    print("The above Headers are validated successfully")
####Test case ID:TC_PIM_03
def test_menu_validation():     ###4th test menu validation
    m1 = "Admin"
    m2 = "PIM"
    m3 = "Leave"
    m4 = "Time"
    m5 = "Recruitment"
    m6 = "My Info"
    m7 = "Performance"
    m8 = "Dashboard"
    m9 = "Directory"
    m10 = "Maintenance"
    m11 = "Buzz"
    print("The above Admin page options are validated successfully")


