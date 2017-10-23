from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import os


# 'General' tab
def general_tab(driver):
    # set Status to Enable
    driver.find_element_by_css_selector("div#tab-general input[name=status]").click()
    # input Name = "test product"
    driver.find_element_by_css_selector("div#tab-general input[name='name[en]']").send_keys("test product")
    # enter Code = "12345"
    driver.find_element_by_css_selector("div#tab-general input[name=code]").send_keys("12345")
    # uncheck Root and check "Rubber Ducks" category
    driver.find_element_by_css_selector("div#tab-general input[data-name=Root]").click()
    driver.find_element_by_css_selector("div#tab-general input[data-name='Rubber Ducks']").click()
    # select "Rubber Ducks" in Default Category select
    select = Select(driver.find_element_by_name("default_category_id"))
    select.select_by_visible_text("Rubber Ducks")
    # check Gender to "Unisex"
    driver.find_element_by_css_selector("div#tab-general input[name='product_groups[]'][value='1-3']").click()
    # set Quantity to 12
    quantity = driver.find_element_by_css_selector("div#tab-general input[name=quantity]")
    ActionChains(driver).move_to_element(quantity).double_click(quantity).perform()
    quantity.send_keys("12")
    ActionChains(driver).move_by_offset(120,120).click().perform()
    # Upload Images from the current directory
    cwd = os.getcwd()
    path = cwd + "/ball.png"
    driver.find_element_by_css_selector("div#tab-general input[name='new_images[]']").send_keys(path)
    # set Date Valid From to "15.11.2016"
    driver.find_element_by_css_selector("div#tab-general input[name=date_valid_from]").send_keys("15.11.2016")
    # set Date Valid To to "15.12.2017"
    driver.find_element_by_css_selector("div#tab-general input[name=date_valid_to]").send_keys("15.12.2017")


def information_tab(driver):
    # select the last element in Manufacturer select
    select = Select(driver.find_element_by_css_selector("div#tab-information [name=manufacturer_id]"))
    select.select_by_index(len(select.options)-1)
    # select the last element in Supplier select
    select = Select(driver.find_element_by_css_selector("div#tab-information [name=supplier_id]"))
    select.select_by_index(len(select.options)-1)
    # input Keyword
    driver.find_element_by_css_selector("div#tab-information [name=keywords]").send_keys("test keyword")
    # enter text "small ball" to Short Description
    driver.find_element_by_css_selector("div#tab-information [name='short_description[en]']").send_keys("small ball")
    # enter text to Description text area
    driver.find_element_by_css_selector("div#tab-information span.input-wrapper "
                                        "div.trumbowyg-editor").send_keys("This is a ball")
    # input Head Title
    driver.find_element_by_css_selector("div#tab-information [name='head_title[en]']").send_keys("Color Ball")
    # input Meta Description
    driver.find_element_by_css_selector("div#tab-information [name='meta_description[en]']").send_keys("meta")


def prices_tab(driver):
    # set Purchase Price to 5 US Dollars
    purchase = driver.find_element_by_css_selector("div#tab-prices input[name=purchase_price]")
    ActionChains(driver).move_to_element(purchase).click().send_keys(Keys.UP * 5).perform()
    select = Select(driver.find_element_by_name("purchase_price_currency_code"))
    select.select_by_visible_text("US Dollars")
    # set Price to 5 USD
    driver.find_element_by_css_selector("div#tab-prices input[name='prices[USD]']").send_keys("50")


# main part
driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

# open Catalog menu
driver.find_element_by_css_selector("#box-apps-menu a[href$=catalog]").click()

# click on "Add New Product" button
driver.find_element_by_css_selector("td#content a[href$=edit_product]").click()

# fill General tab
general_tab(driver)

# open Information tab
driver.find_element_by_css_selector("td#content div.tabs ul.index a[href$=tab-information]").click()
WebDriverWait(driver, 10)
# fill Information tab
information_tab(driver)

# open Prices tab
driver.find_element_by_css_selector("td#content div.tabs ul.index a[href$=tab-prices]").click()
WebDriverWait(driver, 10)
# fill Prices tab
prices_tab(driver)

# press Save button
driver.find_element_by_css_selector("td#content span.button-set [name=save]").click()
WebDriverWait(driver, 10)

# verify that the added product appears in Catalog
table_list = driver.find_elements_by_css_selector("td#content table.dataTable tr.row")
flag = 0
for i in range(len(table_list)):
    if table_list[i].text == "test product":
        print("New product is added to Catalog")
        flag = 1
        break
if flag == 0:
    print("New product is NOT added to Catalog")

driver.quit()
