from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost/litecart/admin/")

#login
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

menu_list = driver.find_element_by_id("box-apps-menu")
links = menu_list.find_elements_by_id("app-")

for i in range(len(links)):
    links[i].click()
    driver.find_element_by_css_selector("td#content h1")
    submenu_list = driver.find_elements_by_css_selector("li#app- .docs .name")

    for j in range(len(submenu_list)-1):
        submenu_list[j+1].click()
        submenu_list = driver.find_elements_by_css_selector("li#app- .docs .name")

    menu_list = driver.find_element_by_id("box-apps-menu")
    links = menu_list.find_elements_by_id("app-")

driver.quit()