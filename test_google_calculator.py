import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    firefox_driver_binary = "./drivers/geckodriver.exe"
    ser_firefox = FirefoxService(firefox_driver_binary)
    firefox_options = FireFoxOptions()
    firefox_options.add_argument("--width=375")
    firefox_options.add_argument("--height=812")
    firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0"
                                                                 "(iPhone; CPU iPhon OS 15_4 like Mac OS X) "
                                                                 "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                                                                 "Version/14.0.3 Mobile/15E148 Safari/604.1")
    driver = webdriver.Firefox(service=ser_firefox ,options=firefox_options)
    yield driver
    driver.close()


def test_google_page_title(driver):
    driver.get('https://www.google.com')
    title = driver.title
    assert title == str.title("google")


# def test_addition_of_2_and_5(driver):
#     driver.get('https://www.google.com')
#     # css_selector, xpath
#     search_field = driver.find_element(By.NAME, "q")
#     search_field.click()
#     search_field.send_keys("2 + 5")
#     search_field.send_keys(Keys.ENTER)
#
#     ans_selector = "#cwos"

    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,ans_selector)))
    # actual_field = driver.find_element(By.CSS_SELECTOR,ans_selector)

    # actual_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ans_selector)))
    #
    # assert actual_field.text == str(7)
    #
    # time.sleep(3)

#
# calc_numbers_input = [("2 + 5", 7), ("3 + 6", 9), ("12 + -1", 11), ("6*9", 40)]
# message_for_calc_numbers_input = [f"Tesing {expected} = {ans}" for expected, ans in calc_numbers_input]

#
# @pytest.mark.parametrize(
#     "test_input,expected_output",
#     [("2 + 5", 7), ("3 + 6", 9), ("12 + -1", 11), ("6*9", 40)],
#     ids=message_for_calc_numbers_input
# )
# def test_addition_of_2_and_5(driver, test_input, expected_output):
#     driver.get('https://www.google.com')
#     # css_selector, xpath
#     search_field = driver.find_element(By.NAME, "q")
#     search_field.click()
#     search_field.send_keys(test_input)
#     search_field.send_keys(Keys.ENTER)
#
#     ans_selector = "#cwos"
#
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,ans_selector)))
#     # actual_field = driver.find_element(By.CSS_SELECTOR,ans_selector)
#
#     actual_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ans_selector)))
#
#     assert actual_field.text == str(expected_output)
#
#     time.sleep(3)
#
#
# def test_youtube_search_and_play_video(driver):
#     driver.get("https://www.youtube.com/")
#     search_field = driver.find_element(By.NAME, "search_query")
#     search_option_selector = "ytd-video-renderer.ytd-item-section-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2) > yt-formatted-string:nth-child(2)"
#     search_field.click()
#     time.sleep(1)
#     search_field.send_keys("testing qa automation")
#     search_field.send_keys(Keys.ENTER)
#
#     first_elem = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, search_option_selector)))
#
#     first_elem.click()
#
#     first_elem_video_selector = ".video-stream"
#     first_elem_video = WebDriverWait(driver, 10) \
#         .until(EC.presence_of_element_located((By.CSS_SELECTOR, first_elem_video_selector)))
#     time.sleep(4)
#
#     first_elem_video.click()
#
#     first_elem_video_title_selector = "yt-formatted-string.ytd-video-primary-info-renderer:nth-child(1)"
#     first_elem_video_title = WebDriverWait(driver, 10) \
#         .until(EC.presence_of_element_located((By.CSS_SELECTOR, first_elem_video_title_selector)))
#
#     assert first_elem_video_title.text == "What is Automated Testing?"
#
#     time.sleep(5)