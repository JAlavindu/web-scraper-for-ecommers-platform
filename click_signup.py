from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_signup_button(driver):

    signup_button = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[starts-with(@class, 'index_module_registryWrapper')]")))
    signup_button.click()