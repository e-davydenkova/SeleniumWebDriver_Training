from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#driver.implicitly_wait(10)

driver.get("http://localhost/litecart/en/")

# adding 3 products to the Cart
for i in range(3):
    # get initial number of products in the Cart
    num = driver.find_element_by_css_selector("div#cart span.quantity").get_attribute("textContent")

    # find a first product from the list and open it
    driver.find_element_by_css_selector("div.content li.product.column.shadow.hover-light").click()

    # check if a selected product is Yellow Duck with a required select field
    if len(driver.find_elements_by_css_selector("div.buy_now [required]")) > 0:
        select = driver.find_element_by_css_selector("div.buy_now select")
        options = select.find_elements_by_tag_name("option")
        options[1].click()

    # add the product to the Cart
    driver.find_element_by_css_selector("div.buy_now button[name=add_cart_product]").click()

    # get number of products in the Cart
    num_updated = driver.find_element_by_css_selector("div#cart span.quantity").get_attribute("textContent")

    # wait while the number of products is updated
    while num >= num_updated:
        WebDriverWait(driver, 10)
        num_updated = driver.find_element_by_css_selector("div#cart span.quantity").get_attribute("textContent")

    # go back to the main page
    driver.execute_script("window.history.go(-1)")

# open the Cart
driver.find_element_by_css_selector("div#cart a.link").click()

# get a list of shortcuts
shortcuts_list = driver.find_elements_by_css_selector("div#box-checkout-cart ul.shortcuts li")

# get a number of rows in a table of products
table_list = driver.find_elements_by_css_selector("div#order_confirmation-wrapper table.dataTable.rounded-corners tr")

# choose all products except the last (which has no shortcut) by a shortcut and remove them
for i in range(len(shortcuts_list)-1):
    # click on a shortcut
    driver.find_element_by_css_selector("div#box-checkout-cart ul.shortcuts li a").click()

    # press Remove button
    driver.find_element_by_css_selector("div#box-checkout-cart button[name=remove_cart_item]").click()

    # check an updated number of rows in a table of products
    table_list_updated = driver.find_elements_by_css_selector("div#order_confirmation-wrapper table.dataTable.rounded-corners tr")

    # wait while the table is updated
    while len(table_list_updated) >= len(table_list):
        wait = WebDriverWait(driver, 10)
        table_list_updated = driver.find_elements_by_css_selector(
            "div#order_confirmation-wrapper table.dataTable.rounded-corners tr")

# remove the last product
driver.find_element_by_css_selector("div#box-checkout-cart form[name=cart_form] button[name=remove_cart_item]").click()
if len(driver.find_elements_by_css_selector(
        "div#box-checkout-cart form[name=cart_form] button[name=remove_cart_item]")) > 0:
    WebDriverWait(driver, 10)
    driver.find_element_by_css_selector(
        "div#box-checkout-cart form[name=cart_form] button[name=remove_cart_item]").click()

# check that there is no table on the page
while len(driver.find_elements_by_css_selector("div#order_confirmation-wrapper table.dataTable.rounded-corners")) > 0:
    WebDriverWait(driver, 10)

driver.quit()
