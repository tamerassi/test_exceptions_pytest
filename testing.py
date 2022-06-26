import pytest


@pytest.fixture()
def driver() :

    chrome_driver_binary = "./drivers/chromedriver.exe"
    ser_chrome = ChromeService(chrome_driver_binary)
    driver = webdriver.Chrome(service=ser_chrome)
    yield driver
    driver.close()
