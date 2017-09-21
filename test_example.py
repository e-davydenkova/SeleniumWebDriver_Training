import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Safari()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    WebDriverWait(driver, 10)
#    driver.find_element_by_name("q").send_keys("webdriver")
#    driver.find_element_by_name("btnG").click()
#    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))

# Вопрос тренеру: тест отрабатывает c результатом "1 test passed", я вижу, что браузер Safari запускается,
# но по окончании окно браузера не закрывается, а показывает домашнюю страницу. Это ожидаемо? Или что-то не так?