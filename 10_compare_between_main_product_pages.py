import pytest
from selenium import webdriver
import re

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/en/")
    request.addfinalizer(wd.quit)
    return wd


# check that product names are identical on the main page and on product page
def test_product_names(driver):

    # get a product name on the main page
    main_name = driver.find_element_by_css_selector("#box-campaigns div li.product.column.shadow.hover-light .name").text

    # get a product name on a product page
    driver.find_element_by_css_selector("#box-campaigns div li.product.column.shadow.hover-light").click()
    product_name = driver.find_element_by_css_selector("#box-product .title").text

    assert main_name == product_name, "Product names on the main page and on product page are NOT identical"


# check that prices (regular and campaign) are identical on the main page and on product page
def test_prices(driver):

    prices = driver.find_element_by_css_selector("#box-campaigns div li.product.column.shadow.hover-light div.price-wrapper")
    # get a regular price on the main page
    main_regular_price = prices.find_element_by_css_selector(".regular-price").text

    # get a campaign price on the main page
    main_campaign_price = prices.find_element_by_css_selector(".campaign-price").text

    # open the product page
    driver.find_element_by_css_selector("#box-campaigns div li.product.column.shadow.hover-light").click()

    # get a regular price on a product page
    product_regular_price = driver.find_element_by_css_selector("#box-product .price-wrapper .regular-price").text

    # get a campaign price on a product page
    product_campaign_price = driver.find_element_by_css_selector("#box-product .price-wrapper .campaign-price").text

    assert main_regular_price == product_regular_price, "Regular prices on the main page and on the product page " \
                                                        "are NOT identical"
    assert main_campaign_price == product_campaign_price, "Campaign prices on the main page and on the product page " \
                                                        "are NOT identical"


# check color of regular and campaign prices and their attributes on the main page
def test_colors_main_page(driver):
    prices = driver.find_element_by_css_selector("#box-campaigns div li.product.column.shadow.hover-light div.price-wrapper")

    # get a color of the regular price on the main page
    regular_color = prices.find_element_by_css_selector(".regular-price").value_of_css_property("color")

    # verify that the regular price is grey (values of R,G,B are identical)
    color_list = re.findall('\d+',regular_color)
    assert(color_list[0] == color_list[1] == color_list[2]), "The regular price on the main page is NOT grey"

    # get a color of the campaign price on the main page
    campaign_color = prices.find_element_by_css_selector(".campaign-price").value_of_css_property("color")

    # verify that the campaign price is red (values of G and B are 0)
    color_list = re.findall('\d+',campaign_color)
    assert (color_list[1] == '0') and (color_list[2] == '0'), "The campaign price on the main page is NOT red"

    regular_attr = prices.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
    assert regular_attr == 'line-through', "Regular price is NOT line-through on the main page"

    campaign_attr = prices.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    assert (campaign_attr == 'bold') or (campaign_attr >= '700'), "Campaign price is NOT bold on the main page"


# check color of regular and campaign prices and their attributes on the product page
def test_colors_product_page(driver):
    # open the product page
    driver.find_element_by_css_selector("#box-campaigns div li.product.column.shadow.hover-light").click()

    prices = driver.find_element_by_css_selector("#box-product .price-wrapper")

    # get a color of the regular price on the main page
    regular_color = prices.find_element_by_css_selector(".regular-price").value_of_css_property("color")

    # verify that the regular price is grey (values of R,G,B are identical)
    color_list = re.findall('\d+', regular_color)
    assert (color_list[0] == color_list[1] == color_list[2]), "The regular price on the product page is NOT grey"

    # get a color of the campaign price on the main page
    campaign_color = prices.find_element_by_css_selector(".campaign-price").value_of_css_property("color")

    # verify that the campaign price is red (values of G and B are 0)
    color_list = re.findall('\d+', campaign_color)
    assert (color_list[1] == '0') and (color_list[2] == '0'), "The campaign price on the product page is NOT red"

    # verify that the regular price is line-through
    regular_attr = prices.find_element_by_css_selector(".regular-price").value_of_css_property(
        "text-decoration-line")
    assert regular_attr == 'line-through', "Regular price is NOT line-through on the product page"

    # verify that the campaign price is bold
    campaign_attr = prices.find_element_by_css_selector(".campaign-price").value_of_css_property(
        "font-weight")
    assert (campaign_attr == 'bold') or (campaign_attr >= '700'), "Campaign price is NOT bold on the product page"


# check that campaign price is bigger than regular prise on the main and product pages
def test_size_comparison(driver):
    prices = driver.find_element_by_css_selector("#box-campaigns div li.product.column.shadow.hover-light div.price-wrapper")

    regular_size = prices.find_element_by_css_selector(".regular-price").size
    campaign_size = prices.find_element_by_css_selector(".campaign-price").size
    assert (campaign_size['height'] > regular_size['height']) and \
           (campaign_size['width'] > regular_size['width']), \
        "Size of campaign price is NOT bigger than size of regular price on the main page"

    # open the product page
    driver.find_element_by_css_selector("#box-campaigns div li.product.column.shadow.hover-light").click()
    prices = driver.find_element_by_css_selector("#box-product .price-wrapper")

    regular_size = prices.find_element_by_css_selector(".regular-price").size
    campaign_size = prices.find_element_by_css_selector(".campaign-price").size
    assert (campaign_size['height'] > regular_size['height']) and \
           (campaign_size['width'] > regular_size['width']), \
        "Size of campaign price is NOT bigger than size of regular price on the product page"
