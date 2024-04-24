
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
driver.implicitly_wait(10)

text_box = driver.find_element(by=By.NAME, value="my-text")

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
time.sleep(5)

text_box.send_keys("Selenium")
time.sleep(5)

submit_button.click()
time.sleep(5)
message = driver.find_element(by=By.ID, value="message")
text = message.text

time.sleep(30)


driver.quit()