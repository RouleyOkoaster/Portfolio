from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    input=browser.find_element(By.TAG_NAME, "input")
    x = int(browser.find_element(By.ID, "input_value").text)
    input.send_keys(str(math.log(abs(12*math.sin(x)))))
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(7)
    browser.quit()