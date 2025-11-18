from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_signup_button(driver):

    signup_button = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")

    signup_button.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'iweb-dialog')]")))