from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)


    is_text_in_element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    if (is_text_in_element):
        button = browser.find_element(By.ID, "book")
        button.click()

        button1 = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "solve"))
        )

        field = browser.find_element(By.ID, "answer")
        x = browser.find_element(By.ID, "input_value").text
        field.send_keys(str(math.log(12*math.sin(int(x)))))

        button1.click()

finally:
    time.sleep(7)
    browser.quit()
