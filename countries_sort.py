from selenium import webdriver


# check that a country list is sorted
def check_country_list():
    countries = []

    # list of countries
    countries_list = driver.find_elements_by_css_selector("table.dataTable tr.row td:nth-child(5)")
    # list of zones
    zones_list = driver.find_elements_by_css_selector("table.dataTable tr.row td:nth-child(6)")

    for i in range(len(countries_list)):
        s = countries_list[i].get_attribute("textContent")
        # creating a list of country names (strings)
        countries.append(s)

        # check that a sub-country list for each country with Zone number != 0 is sorted
        subcountries = []
        if zones_list[i].get_attribute("textContent") != "0":
            countries_list[i].find_element_by_css_selector("a").click()

            subcountries_list = driver.find_elements_by_css_selector("table#table-zones tbody td:nth-child(3)")
            for j in range(len(subcountries_list)):
                sub = subcountries_list[j].get_attribute("textContent")
                # creating a list of sub-counties with removing the last empty element
                if sub != '':
                    subcountries.append(sub)

            # go back
            driver.execute_script("window.history.go(-1)")
            countries_list = driver.find_elements_by_css_selector("table.dataTable tr.row td:nth-child(5)")
            zones_list = driver.find_elements_by_css_selector("table.dataTable tr.row td:nth-child(6)")

            subcountries_sorted = list(subcountries)
            subcountries_sorted.sort()
#            print(subcountries_sorted)
#            print(subcountries)
            print("Sub-country list is sorted: ", subcountries_sorted == subcountries)

    countries_sorted = list(countries)
    countries_sorted.sort()
    print("Country list is sorted: ", countries_sorted == countries)

    return countries_sorted == countries


# check that a geo zone list is sorted for each country
def check_geozones():

    # list of countries
    countries_list = driver.find_elements_by_css_selector("table.dataTable tr.row td:nth-child(3) a")
    for i in range(len(countries_list)):
        countries_list[i].click()
        geozones = []

        # list of geo zones for a selected country
        geozones_list = driver.find_elements_by_css_selector("#table-zones tbody td:nth-child(3) [selected]")
        for j in range(len(geozones_list)):
            sub = geozones_list[j].get_attribute("textContent")
            geozones.append(sub)

        geozones_sorted = list(geozones)
        geozones_sorted.sort()
#        print(geozones_sorted)
#        print(geozones)
        print("Geozone list is sorted: ",geozones_sorted == geozones)

        # go back
        driver.execute_script("window.history.go(-1)")
        countries_list = driver.find_elements_by_css_selector("table.dataTable tr.row td:nth-child(3) a")


# main block
driver = webdriver.Chrome()

# login
driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

# task 9_1: check a country list and sub-country lists
check_country_list()

# task 9_2: check geo zones lists
driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
check_geozones()

driver.quit()