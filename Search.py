import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("cu")
time.sleep(3)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)
print(count)
assert count > 0

