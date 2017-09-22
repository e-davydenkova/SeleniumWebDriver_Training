from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Safari()

driver.get("http://localhost/litecart/admin/")

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

WebDriverWait(driver, 600)

driver.quit()