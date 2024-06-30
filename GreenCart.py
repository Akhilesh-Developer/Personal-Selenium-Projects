import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
cartItems = driver.find_elements(By.XPATH,"//div[@class='product']")
for item in cartItems:
    item.find_element(By.XPATH,"div/button").click()   # here path linking tok place    # loop will run till depending on item number in cartItems
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder ='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver, 10)                              #here explicit wait is given with help of WebDriverWait class that takes driver and time as arguments
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
dropdown = Select(driver.find_element(By.XPATH,"//div/select"))
dropdown.select_by_visible_text("India")
driver.find_element(By.XPATH,"//input[@type ='checkbox']").click()
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()







