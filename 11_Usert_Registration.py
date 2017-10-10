from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://localhost/litecart/en/")

def get_unique_email():
    return str(time.time()) + "@test.com"

for i in range(2):
    # click on 'New customers click here' link
    driver.find_element_by_css_selector("#box-account-login [name=login_form] a").click()

    # fill in registration form
    driver.find_element_by_css_selector("#create-account input[name=firstname]").send_keys("Test")
    driver.find_element_by_css_selector("#create-account input[name=lastname]").send_keys("Test")
    driver.find_element_by_css_selector("#create-account input[name=address1]").send_keys("Address")
    driver.find_element_by_css_selector("#create-account input[name=postcode]").send_keys("11111")
    driver.find_element_by_css_selector("#create-account input[name=city]").send_keys("City")
    driver.find_element_by_css_selector("#create-account span.select2").click()
    driver.find_element_by_css_selector("span.select2-search.select2-search--dropdown input").send_keys("United States" + Keys.ENTER)
    driver.find_element_by_css_selector("#create-account input[name=email]").send_keys(get_unique_email())
    driver.find_element_by_css_selector("#create-account input[name=phone]").send_keys("+123456789")
    driver.find_element_by_css_selector("#create-account input[name=password]").send_keys("1")
    driver.find_element_by_css_selector("#create-account input[name=confirmed_password]").send_keys("1")

    # press 'Create Account' button
    driver.find_element_by_css_selector("#create-account button[name=create_account]").click()

    # logout by pressing 'Logout' link
    driver.find_element_by_css_selector("#box-account a[href$=logout]").click()

driver.quit()