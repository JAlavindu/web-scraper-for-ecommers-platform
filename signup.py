from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

def signup_test(phone_number, OTP):

    driver.get("https://www.daraz.lk/#?")
    signUpButton = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
    print(signUpButton.is_displayed())
    signUpButton.click()
    time.sleep(5)

    phone_input = driver.find_element(By.XPATH, "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter your phone number']")
    phone_input.send_keys(phone_number)




driver.quit()
