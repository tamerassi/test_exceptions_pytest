from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

usrname = "student"
password = "Password123"
url= "https://practicetestautomation.com/practice-test-login/"

chrome_driver_binary = "./drivers/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_binary)

driver.get(url)
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys(usrname)
sleep(3)
# driver.find_element(By.ID, "identifierNext").click()
# sleep(2)
driver.find_element(By.NAME, "password").send_keys(password)
sleep(2)
driver.find_element(By.ID,"submit").click()

loggingis = driver.find_element(By.CSS_SELECTOR,".post-header.post-title")

print(loggingis.get_attribute("innerHTML"))


driver.quit()