from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def new_window_appears(old_windows):
#     new_windows = driver.window_handles
#
#     if len(new_windows) > len(old_windows):
#         handle = [x for x in new_windows if (x not in old_windows)]
#         return handle     # error: return a list but need to have WebDriver list - ???
#     else:
#         return False


# main part
driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

# open Countries menu
driver.find_element_by_css_selector("#box-apps-menu a[href$=countries]").click()

# press "Add New Country" button
driver.find_element_by_css_selector("td#content a[href$=edit_country]").click()

# collect all elements containing external links
links_list = driver.find_elements_by_css_selector("td#content a i.fa.fa-external-link")

for i in range(len(links_list)):
    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    # open a new window
    links_list[i].click()

    # wait for a new window appears
#    new_window = wait.until(new_window_appears(old_windows))
    wait = WebDriverWait(driver, 10)
    wait.until(EC.new_window_is_opened)

    new_windows = driver.window_handles

    if len(new_windows) > len(old_windows):
        handle = [x for x in new_windows if (x not in old_windows)]
        new_window = handle[0]

    driver.switch_to_window(new_window)
    print(driver.title)
    driver.close()
    driver.switch_to_window(main_window)

driver.quit()