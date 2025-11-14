# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from anticaptchaofficial.geetestproxyless import *
#
# ANTI_API_KEY = "2a0d3dd4c7e7c4851b796dc302daa8c1"
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# def signup_test():
#     driver.get("https://www.daraz.lk/#?")
#     signUpButton = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
#     print(signUpButton.is_displayed())
#     signUpButton.click()
#
#     input_phone_num()
#
#     try:
#         checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'iweb-checkbox-icon')]")))
#         driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)  # Scroll into view
#         driver.execute_script("arguments[0].click();", checkbox)
#         print("Checkbox clicked")
#     except Exception as e:
#         print(f"Checkbox was not clickable: {e}")
#
#     time.sleep(2)
#
#     try:
#         otp_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
#                                        "//div[contains(@class, 'index_module_otpText')]")))
#         driver.execute_script("arguments[0].scrollIntoView(true);", otp_button)
#         driver.execute_script("arguments[0].click();", otp_button)
#         print("OTP button clicked")
#     except Exception as e:
#         print(f"OTP button was not clickable: {e}")
#         driver.quit()
#         return
#
#     try:
#         iframe = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'captcha')]"))
#         )
#         driver.switch_to.frame(iframe)
#
#         print("🟡 Extracting GeeTest config...")
#
#         # Read GeeTest init JSON object from page
#         geetest_config = driver.execute_script("""
#                 return window.initData ? window.initData : window.conf ? window.conf : null;
#             """)
#
#         if geetest_config is None:
#             print("❌ Could not detect GeeTest config")
#             return
#
#         print(json.dumps(geetest_config, indent=2))
#
#         gt = geetest_config["gt"]
#         challenge = geetest_config["challenge"]
#
#         print("GT:", gt)
#         print("Challenge:", challenge)
#
#         # Solve via AntiCaptcha
#         solution = solve_geetest(gt, challenge, driver.current_url)
#
#         if solution is None:
#             print("❌ Failed to solve GeeTest")
#             driver.quit()
#             return
#
#         print("🟢 Injecting solved captcha into GeeTest...")
#
#         driver.execute_script("""
#                 document.getElementById("geetest_challenge").value = arguments[0];
#                 document.getElementById("geetest_validate").value = arguments[1];
#                 document.getElementById("geetest_seccode").value = arguments[2];
#             """, solution["challenge"], solution["validate"], solution["seccode"])
#
#         print("🟢 Captcha bypassed!")
#
#         # Submit
#         driver.execute_script("document.querySelector('button').click()")
#
#
#
#
#         print("Slider captcha solved")
#     except Exception as e:
#         print(f"Slider captcha could not be solved: {e}")
#         driver.quit()
#         return
#
#
#     time.sleep(5)
#     driver.quit()
#
# def input_phone_num():
#     phone_num = input("Enter your phone number: ")
#     phone_input = driver.find_element(By.XPATH, "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter your phone number']")
#     phone_input.send_keys(phone_num)
#
# def input_otp():
#     otp = input("Enter the OTP sent to your phone: ")
#     otp_input = driver.find_element(By.XPATH, "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter the OTP']")
#     otp_input.send_keys(otp)
#
# def solve_geetest(gt, challenge, url):
#     solver = geetestProxyless()
#     solver.set_verbose(1)
#     solver.set_key(ANTI_API_KEY)
#     solver.set_website_url(url)
#     solver.set_gt_key(gt)
#     solver.set_challenge(challenge)
#
#     print("🟡 Sending to AntiCaptcha...")
#
#     result = solver.solve_and_return_solution()
#
#     if result != 0:
#         print("🟢 AntiCaptcha solved it!")
#         return result
#     else:
#         print("🔴 AntiCaptcha Error:", solver.error_code)
#         return None
#
#
#


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anticaptchaofficial.geetestproxyless import *

ANTI_API_KEY = "2a0d3dd4c7e7c4851b796dc302daa8c1"  # Replace with your actual key

driver = webdriver.Chrome()
driver.maximize_window()


def signup_test():
    driver.get("https://www.daraz.lk/#?")
    signUpButton = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
    print(signUpButton.is_displayed())
    signUpButton.click()

    input_phone_num()

    # Click checkbox
    try:
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'iweb-checkbox-icon')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        driver.execute_script("arguments[0].click();", checkbox)
        print("Checkbox clicked")
    except Exception as e:
        print(f"Checkbox was not clickable: {e}")

    time.sleep(2)

    # Click OTP button
    try:
        otp_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'index_module_otpText')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", otp_button)
        driver.execute_script("arguments[0].click();", otp_button)
        print("OTP button clicked")
    except Exception as e:
        print(f"OTP button was not clickable: {e}")
        driver.quit()
        return

    # Handle GeeTest captcha
    try:
        # Wait for captcha iframe
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'captcha')]"))
        )

        # Get the page URL before switching to iframe
        page_url = driver.current_url

        driver.switch_to.frame(iframe)
        print("🟡 Extracting GeeTest config...")

        # Extract GeeTest configuration
        geetest_config = driver.execute_script("""
            return window.initData ? window.initData : window.conf ? window.conf : null;
        """)

        if geetest_config is None:
            print("❌ Could not detect GeeTest config")
            driver.switch_to.default_content()
            driver.quit()
            return

        print("GeeTest Config:", json.dumps(geetest_config, indent=2))

        gt = geetest_config.get("gt")
        challenge = geetest_config.get("challenge")

        if not gt or not challenge:
            print("❌ Missing GT or Challenge parameter")
            driver.switch_to.default_content()
            driver.quit()
            return

        print(f"GT: {gt}")
        print(f"Challenge: {challenge}")

        # Switch back to main content
        driver.switch_to.default_content()

        # Solve captcha using AntiCaptcha
        solution = solve_geetest(gt, challenge, page_url)

        if solution is None:
            print("❌ Failed to solve GeeTest")
            driver.quit()
            return

        print("🟢 GeeTest solved successfully!")
        print(f"Solution: {json.dumps(solution, indent=2)}")

        # Switch back to iframe to inject solution
        driver.switch_to.frame(iframe)

        # Inject the solution into the page
        driver.execute_script("""
            if (typeof window.captchaObj !== 'undefined') {
                window.captchaObj.getValidate = function() {
                    return {
                        geetest_challenge: arguments[0],
                        geetest_validate: arguments[1],
                        geetest_seccode: arguments[2]
                    };
                };
            }
        """, solution["geetest_challenge"], solution["geetest_validate"], solution["geetest_seccode"])

        print("🟢 Captcha solution injected!")

        # Switch back to main content
        driver.switch_to.default_content()

        # Wait a moment for the captcha to be validated
        time.sleep(3)

        # Now input OTP
        input_otp()

        print("Process completed successfully!")

    except Exception as e:
        print(f"Error handling captcha: {e}")
        driver.switch_to.default_content()
        driver.quit()
        return

    time.sleep(5)
    driver.quit()


def input_phone_num():
    phone_num = input("Enter your phone number: ")
    phone_input = driver.find_element(
        By.XPATH,
        "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter your phone number']"
    )
    phone_input.send_keys(phone_num)


def input_otp():
    otp = input("Enter the OTP sent to your phone: ")
    otp_input = driver.find_element(
        By.XPATH,
        "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter the OTP']"
    )
    otp_input.send_keys(otp)

    # Submit OTP
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit') or contains(text(),'Verify')]")
    submit_button.click()


def solve_geetest(gt, challenge, url):
    solver = geetestProxyless()
    solver.set_verbose(1)
    solver.set_key(ANTI_API_KEY)
    solver.set_website_url(url)
    solver.set_gt_key(gt)
    solver.set_challenge_key(challenge)

    print("🟡 Sending to AntiCaptcha...")

    try:
        solution = solver.solve_and_return_solution()

        if solution != 0 and isinstance(solution, dict):
            print("🟢 AntiCaptcha solved it!")
            return solution
        else:
            print(f"🔴 AntiCaptcha Error: {solver.error_code}")
            return None
    except Exception as e:
        print(f"🔴 Exception during solve: {e}")
        return None