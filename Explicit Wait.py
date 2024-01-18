import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
#Implicitly Wait is like a Global wait if the elements does not load
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("cu")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)

assert count > 0
# add items to cart with the next step
for result in results:
    result.find_element(By.XPATH, "div/button").click()

# Go to Cart page
driver.find_element(By.CLASS_NAME, "cart-icon").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
promocode = "rahulshettyacademy"
driver.find_element(By.CLASS_NAME, "promoCode").send_keys(promocode)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#Explicit wait is specific to the intance where we have to wait for more than the globally defined wait (implicit wait) so that the time is saved by not unnecessarily waiting
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text
      )