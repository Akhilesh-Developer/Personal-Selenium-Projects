from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
cards = driver.find_elements(By.XPATH,"//div[@class = 'card h-100']")

for phones in cards:
    name = phones.find_element(By.XPATH,"div/h4/a").text
    if name == "Blackbery":
        phones.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
# assert "India" == driver.find_element(By.LINK_TEXT,"India")
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type = 'submit']").click()
successMsg = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you! " in successMsg