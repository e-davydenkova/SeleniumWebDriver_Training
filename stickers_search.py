from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost/litecart/en/")

products_list = driver.find_elements_by_css_selector("div li.product.column.shadow.hover-light")
#stickers_list = driver.find_elements_by_css_selector("div li.product.column.shadow.hover-light .sticker")

for i in range(len(products_list)):
    sticker = products_list[i].find_elements_by_class_name("sticker")
    if len(sticker) != 1:
        print("There is not 1 sticker for a ",products_list[i]," element")

driver.quit()