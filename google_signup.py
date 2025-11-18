from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import open_daraz

def signup_with_google(driver):
    print("Signing up with Google account...")
    check_box = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'iweb-checkbox-icon')]"))
    )
    check_box.click()
    print("checkbox clicked")
    google_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'index_module_buttonItem')]")
        )
    )

    print(google_button.is_displayed())
    google_button.click()

    print("Google sign-up button clicked!")