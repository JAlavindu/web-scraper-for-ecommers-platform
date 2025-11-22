import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Global driver (same behavior as your original script)
driver = None

def daraz_open():
    global driver

    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")

    # Start undetected chrome
    driver = uc.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://www.daraz.lk/")

    # Wait for body to ensure website loaded
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    print("✅ Daraz website opened successfully")
    return driver
