from unittest import TestCase
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, \
    StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService


class TestExceptionsWithSelenium(TestCase):

    def setUp(self):
        chrome_driver_binary = "./drivers/chromedriver.exe"
        ser_chrome = ChromeService(chrome_driver_binary)
        self.driver = webdriver.Chrome(service=ser_chrome)
        # self.addCleanup(self.driver.close)

    def tearDown(self):
        self.driver.close()

# Test case 1: NoSuchElementException
    def test_row_two_input(self):
        self.driver.get('https://practicetestautomation.com/practice-test-exceptions/')
        add_btn = self.driver.find_element(By.CSS_SELECTOR, '#add_btn')
        add_btn.click()
        try:
            row_2_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#row2 > input')))
            with self.subTest("Testing Row 2 input field is displayed"):
                self.assertTrue(row_2_input.is_displayed())
        except NoSuchElementException:
            self.fail()

    # Test case 2: ElementNotInteractableException
    def test_save_button(self):
        self.driver.get('https://practicetestautomation.com/practice-test-exceptions/')
        self.driver.maximize_window()
        add_btn = self.driver.find_element(By.CSS_SELECTOR, '#add_btn')
        add_btn.click()
        try:
            row_2_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#row2 > input')))
            with self.subTest("Testing Row 2 input field is displayed"):
                self.assertTrue(row_2_input.is_displayed())
        except NoSuchElementException:
            self.fail()
        with self.subTest("Testing Row 2 saved user input"):
            try:
                row_2_input = self.driver.find_element(By.CSS_SELECTOR, '#row2 > input')
                row_2_input.click()
                row_2_input.send_keys("Burger")
                save_button = self.driver.find_element(By.CSS_SELECTOR, '#row2 > #save_btn')
                save_button.click()
                text_saved = self.driver.find_element(By.CSS_SELECTOR, '#confirmation').text
                self.assertEqual('Row 2 was saved', text_saved)
                time.sleep(5)
            except ElementNotInteractableException:
                self.fail()

    # Test case 3: InvalidElementStateException
    def test_text_changed(self):
        self.test_save_button()

        with self.subTest("Testing change text"):
            edit_button = self.driver.find_element(By.CSS_SELECTOR, '#row2 > #edit_btn')
            edit_button.click()
            try:
                row_2_input = self.driver.find_element(By.CSS_SELECTOR, '#row2 > input')
                row_2_input.click()
                row_2_input.clear()
                row_2_input.send_keys("Carpaccio")
                time.sleep(5)
                save_button = self.driver.find_element(By.CSS_SELECTOR, '#row2 > #save_btn')
                save_button.click()
                text_saved = self.driver.find_element(By.CSS_SELECTOR, '#confirmation').text
                self.assertEqual('Row 2 was saved', text_saved)
                time.sleep(5)
            except InvalidElementStateException:
                self.fail()

# Test case 4: StaleElementReferenceException
    def test_instructions_text_element(self):
        self.driver.get('https://practicetestautomation.com/practice-test-exceptions/')
        self.driver.maximize_window()
        time.sleep(3)
        row1_add_btn = self.driver.find_element(By.CSS_SELECTOR, '#add_btn')
        row1_add_btn.click()
        with self.subTest("Testing instruction text element display"):
            try:
                instruction_text = WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element((By.CSS_SELECTOR, '#instructions')))
                self.assertTrue(instruction_text)
            except StaleElementReferenceException:
                self.fail()

#Test case 5: TimeoutException
    def test_displayed_second_input(self):
        self.driver.get('https://practicetestautomation.com/practice-test-exceptions/')
        self.driver.maximize_window()
        row1_add_btn = self.driver.find_element(By.CSS_SELECTOR, '#add_btn')
        row1_add_btn.click()
        try:
            time.sleep(10)
            row_2_input = self.driver.find_element(By.CSS_SELECTOR, '#row2 > input')
            row_2_input.click()
            with self.subTest("Testing Row 2 input field is displayed"):
                self.assertTrue(row_2_input.is_displayed())
        except TimeoutException :
            self.fail()