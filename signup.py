# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import time
# # from selenium.webdriver.support.wait import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.action_chains import ActionChains
# # from anticaptchaofficial.geetestproxyless import *
# #
# # ANTI_API_KEY = "2a0d3dd4c7e7c4851b796dc302daa8c1"
# #
# # driver = webdriver.Chrome()
# # driver.maximize_window()
# #
# # def signup_test():
# #     driver.get("https://www.daraz.lk/#?")
# #     signUpButton = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
# #     print(signUpButton.is_displayed())
# #     signUpButton.click()
# #
# #     input_phone_num()
# #
# #     try:
# #         checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'iweb-checkbox-icon')]")))
# #         driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)  # Scroll into view
# #         driver.execute_script("arguments[0].click();", checkbox)
# #         print("Checkbox clicked")
# #     except Exception as e:
# #         print(f"Checkbox was not clickable: {e}")
# #
# #     time.sleep(2)
# #
# #     try:
# #         otp_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
# #                                        "//div[contains(@class, 'index_module_otpText')]")))
# #         driver.execute_script("arguments[0].scrollIntoView(true);", otp_button)
# #         driver.execute_script("arguments[0].click();", otp_button)
# #         print("OTP button clicked")
# #     except Exception as e:
# #         print(f"OTP button was not clickable: {e}")
# #         driver.quit()
# #         return
# #
# #     try:
# #         iframe = WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'captcha')]"))
# #         )
# #         driver.switch_to.frame(iframe)
# #
# #         print("🟡 Extracting GeeTest config...")
# #
# #         # Read GeeTest init JSON object from page
# #         geetest_config = driver.execute_script("""
# #                 return window.initData ? window.initData : window.conf ? window.conf : null;
# #             """)
# #
# #         if geetest_config is None:
# #             print("❌ Could not detect GeeTest config")
# #             return
# #
# #         print(json.dumps(geetest_config, indent=2))
# #
# #         gt = geetest_config["gt"]
# #         challenge = geetest_config["challenge"]
# #
# #         print("GT:", gt)
# #         print("Challenge:", challenge)
# #
# #         # Solve via AntiCaptcha
# #         solution = solve_geetest(gt, challenge, driver.current_url)
# #
# #         if solution is None:
# #             print("❌ Failed to solve GeeTest")
# #             driver.quit()
# #             return
# #
# #         print("🟢 Injecting solved captcha into GeeTest...")
# #
# #         driver.execute_script("""
# #                 document.getElementById("geetest_challenge").value = arguments[0];
# #                 document.getElementById("geetest_validate").value = arguments[1];
# #                 document.getElementById("geetest_seccode").value = arguments[2];
# #             """, solution["challenge"], solution["validate"], solution["seccode"])
# #
# #         print("🟢 Captcha bypassed!")
# #
# #         # Submit
# #         driver.execute_script("document.querySelector('button').click()")
# #
# #
# #
# #
# #         print("Slider captcha solved")
# #     except Exception as e:
# #         print(f"Slider captcha could not be solved: {e}")
# #         driver.quit()
# #         return
# #
# #
# #     time.sleep(5)
# #     driver.quit()
# #
# # def input_phone_num():
# #     phone_num = input("Enter your phone number: ")
# #     phone_input = driver.find_element(By.XPATH, "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter your phone number']")
# #     phone_input.send_keys(phone_num)
# #
# # def input_otp():
# #     otp = input("Enter the OTP sent to your phone: ")
# #     otp_input = driver.find_element(By.XPATH, "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter the OTP']")
# #     otp_input.send_keys(otp)
# #
# # def solve_geetest(gt, challenge, url):
# #     solver = geetestProxyless()
# #     solver.set_verbose(1)
# #     solver.set_key(ANTI_API_KEY)
# #     solver.set_website_url(url)
# #     solver.set_gt_key(gt)
# #     solver.set_challenge(challenge)
# #
# #     print("🟡 Sending to AntiCaptcha...")
# #
# #     result = solver.solve_and_return_solution()
# #
# #     if result != 0:
# #         print("🟢 AntiCaptcha solved it!")
# #         return result
# #     else:
# #         print("🔴 AntiCaptcha Error:", solver.error_code)
# #         return None
# #
# #
# #
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import json
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from anticaptchaofficial.geetestproxyless import *
#
# ANTI_API_KEY = "2a0d3dd4c7e7c4851b796dc302daa8c1"  # Replace with your actual key
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
#
# def signup_test():
#     driver.get("https://www.daraz.lk/#?")
#     signUpButton = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
#     print(signUpButton.is_displayed())
#     signUpButton.click()
#
#     input_phone_num()
#
#     # Click checkbox
#     try:
#         checkbox = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'iweb-checkbox-icon')]"))
#         )
#         driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
#         driver.execute_script("arguments[0].click();", checkbox)
#         print("Checkbox clicked")
#     except Exception as e:
#         print(f"Checkbox was not clickable: {e}")
#
#     time.sleep(2)
#
#     # Click OTP button
#     try:
#         otp_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'index_module_otpText')]"))
#         )
#         driver.execute_script("arguments[0].scrollIntoView(true);", otp_button)
#         driver.execute_script("arguments[0].click();", otp_button)
#         print("OTP button clicked")
#     except Exception as e:
#         print(f"OTP button was not clickable: {e}")
#         driver.quit()
#         return
#
#     # Handle GeeTest captcha
#     try:
#         # Wait for captcha iframe
#         iframe = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'captcha')]"))
#         )
#
#         # Get the page URL before switching to iframe
#         page_url = driver.current_url
#
#         driver.switch_to.frame(iframe)
#         print("🟡 Extracting GeeTest config...")
#
#         # Extract GeeTest configuration
#         geetest_config = driver.execute_script("""
#             return window.initData ? window.initData : window.conf ? window.conf : null;
#         """)
#
#         if geetest_config is None:
#             print("❌ Could not detect GeeTest config")
#             driver.switch_to.default_content()
#             driver.quit()
#             return
#
#         print("GeeTest Config:", json.dumps(geetest_config, indent=2))
#
#         gt = geetest_config.get("gt")
#         challenge = geetest_config.get("challenge")
#
#         if not gt or not challenge:
#             print("❌ Missing GT or Challenge parameter")
#             driver.switch_to.default_content()
#             driver.quit()
#             return
#
#         print(f"GT: {gt}")
#         print(f"Challenge: {challenge}")
#
#         # Switch back to main content
#         driver.switch_to.default_content()
#
#         # Solve captcha using AntiCaptcha
#         solution = solve_geetest(gt, challenge, page_url)
#
#         if solution is None:
#             print("❌ Failed to solve GeeTest")
#             driver.quit()
#             return
#
#         print("🟢 GeeTest solved successfully!")
#         print(f"Solution: {json.dumps(solution, indent=2)}")
#
#         # Switch back to iframe to inject solution
#         driver.switch_to.frame(iframe)
#
#         # Inject the solution into the page
#         driver.execute_script("""
#             if (typeof window.captchaObj !== 'undefined') {
#                 window.captchaObj.getValidate = function() {
#                     return {
#                         geetest_challenge: arguments[0],
#                         geetest_validate: arguments[1],
#                         geetest_seccode: arguments[2]
#                     };
#                 };
#             }
#         """, solution["geetest_challenge"], solution["geetest_validate"], solution["geetest_seccode"])
#
#         print("🟢 Captcha solution injected!")
#
#         # Switch back to main content
#         driver.switch_to.default_content()
#
#         # Wait a moment for the captcha to be validated
#         time.sleep(3)
#
#         # Now input OTP
#         input_otp()
#
#         print("Process completed successfully!")
#
#     except Exception as e:
#         print(f"Error handling captcha: {e}")
#         driver.switch_to.default_content()
#         driver.quit()
#         return
#
#     time.sleep(5)
#     driver.quit()
#
#
# def input_phone_num():
#     phone_num = input("Enter your phone number: ")
#     phone_input = driver.find_element(
#         By.XPATH,
#         "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter your phone number']"
#     )
#     phone_input.send_keys(phone_num)
#
#
# def input_otp():
#     otp = input("Enter the OTP sent to your phone: ")
#     otp_input = driver.find_element(
#         By.XPATH,
#         "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter the OTP']"
#     )
#     otp_input.send_keys(otp)
#
#     # Submit OTP
#     submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit') or contains(text(),'Verify')]")
#     submit_button.click()
#
#
# def solve_geetest(gt, challenge, url):
#     solver = geetestProxyless()
#     solver.set_verbose(1)
#     solver.set_key(ANTI_API_KEY)
#     solver.set_website_url(url)
#     solver.set_gt_key(gt)
#     solver.set_challenge_key(challenge)
#
#     print("🟡 Sending to AntiCaptcha...")
#
#     try:
#         solution = solver.solve_and_return_solution()
#
#         if solution != 0 and isinstance(solution, dict):
#             print("🟢 AntiCaptcha solved it!")
#             return solution
#         else:
#             print(f"🔴 AntiCaptcha Error: {solver.error_code}")
#             return None
#     except Exception as e:
#         print(f"🔴 Exception during solve: {e}")
#         return None

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For Alibaba NC Captcha, you'll need anticaptcha's funcaptcha or custom solution
from anticaptchaofficial.funcaptchaproxyless import *

ANTI_API_KEY = "2a0d3dd4c7e7c4851b796dc302daa8c1"

# Setup Chrome with network logging
chrome_options = Options()
chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


def extract_captcha_params_from_network():
    """Extract captcha parameters from network logs"""
    logs = driver.get_log('performance')

    captcha_data = {
        'session_id': None,
        'sig': None,
        'token': None,
        'scene': None,
        'appkey': None
    }

    for entry in logs:
        try:
            log = json.loads(entry['message'])['message']

            if log.get('method') == 'Network.responseReceived':
                response = log.get('params', {}).get('response', {})
                url = response.get('url', '')

                # Look for captcha initialization URLs
                if 'captcha' in url.lower() or 'nc.js' in url.lower():
                    print(f"🔍 Found captcha URL: {url[:100]}...")

                    # Extract parameters from URL
                    if 'secdata' in url:
                        match = re.search(r'secdata=([^&]+)', url)
                        if match:
                            captcha_data['session_id'] = match.group(1)

                    # Try to get response body
                    try:
                        request_id = log['params']['requestId']
                        response_body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': request_id})
                        body = response_body.get('body', '')

                        # Try to parse JSON
                        try:
                            json_data = json.loads(body)
                            print(f"📄 Response data: {json.dumps(json_data, indent=2)[:300]}")

                            # Extract NC Captcha parameters
                            if 'data' in json_data:
                                data = json_data['data']
                                captcha_data['session_id'] = data.get('csessionid') or data.get('sessionId')
                                captcha_data['sig'] = data.get('sig')
                                captcha_data['token'] = data.get('token')
                                captcha_data['scene'] = data.get('scene')

                        except json.JSONDecodeError:
                            pass

                    except Exception as e:
                        pass

        except Exception as e:
            continue

    return captcha_data


def extract_captcha_from_page():
    """Extract captcha parameters directly from page"""
    try:
        # Wait for captcha to load
        time.sleep(3)

        print("🔍 Extracting captcha config from page...")

        # Method 1: Check for NC (NoCaptcha) object
        nc_config = driver.execute_script("""
            // Check for Alibaba NC Captcha
            if (window.NC_Opt) return window.NC_Opt;
            if (window.nc_config) return window.nc_config;
            if (window.noCaptcha) return window.noCaptcha;

            // Check iframes
            var iframes = document.getElementsByTagName('iframe');
            for (var i = 0; i < iframes.length; i++) {
                try {
                    if (iframes[i].contentWindow.NC_Opt) {
                        return iframes[i].contentWindow.NC_Opt;
                    }
                } catch(e) {}
            }

            return null;
        """)

        if nc_config:
            print("✅ Found NC Config:")
            print(json.dumps(nc_config, indent=2))
            return nc_config

        # Method 2: Extract from DOM attributes
        captcha_element = driver.execute_script("""
            var elements = document.querySelectorAll('[data-nc-idx], [id*="nc_"], .nc-container, [class*="nc-"]');
            if (elements.length > 0) {
                var el = elements[0];
                return {
                    'nc-idx': el.getAttribute('data-nc-idx'),
                    'id': el.id,
                    'className': el.className
                };
            }
            return null;
        """)

        if captcha_element:
            print("✅ Found captcha element:")
            print(json.dumps(captcha_element, indent=2))
            return captcha_element

        return None

    except Exception as e:
        print(f"❌ Error extracting captcha: {e}")
        return None


def solve_nc_captcha_manual():
    """Manual slider solving - for testing"""
    try:
        print("\n🎯 Attempting to find slider...")

        # Wait for slider to appear
        time.sleep(3)

        # Try to find the slider in main page or iframe
        slider = None

        # Check main page first
        try:
            slider = driver.find_element(By.CSS_SELECTOR,
                                         ".nc_iconfont.btn_slide, .nc-lang-cnt, [class*='nc_'], [id*='nc_']")
            print("✅ Found slider in main page")
        except:
            print("⚠️ Slider not in main page, checking iframes...")

            # Check iframes
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            for idx, iframe in enumerate(iframes):
                try:
                    driver.switch_to.frame(iframe)
                    slider = driver.find_element(By.CSS_SELECTOR,
                                                 ".nc_iconfont.btn_slide, .nc-lang-cnt, [class*='slider']")
                    print(f"✅ Found slider in iframe {idx}")
                    break
                except:
                    driver.switch_to.default_content()
                    continue

        if slider:
            print("\n⚠️ MANUAL SOLVING REQUIRED")
            print("Please solve the slider captcha manually in the browser")
            print("Press Enter after you've solved it...")
            input()

            driver.switch_to.default_content()
            return True
        else:
            print("❌ Could not find slider element")
            return False

    except Exception as e:
        print(f"❌ Error solving captcha: {e}")
        driver.switch_to.default_content()
        return False


def signup_test():
    try:
        driver.get("https://www.daraz.lk/#?")
        time.sleep(2)

        # Click Sign Up
        print("📝 Clicking Sign Up...")
        signUpButton = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
        signUpButton.click()
        time.sleep(2)

        # Input phone number
        input_phone_num()

        # Click checkbox
        try:
            print("☑️ Clicking checkbox...")
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'iweb-checkbox-icon')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            driver.execute_script("arguments[0].click();", checkbox)
            print("✅ Checkbox clicked")
        except Exception as e:
            print(f"❌ Checkbox error: {e}")

        time.sleep(2)

        # Clear logs before clicking OTP
        driver.get_log('performance')

        # Click OTP button
        try:
            print("🚀 Clicking OTP button...")
            otp_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'index_module_otpText')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", otp_button)
            driver.execute_script("arguments[0].click();", otp_button)
            print("✅ OTP button clicked")
        except Exception as e:
            print(f"❌ OTP button error: {e}")
            return

        # Wait for captcha to load
        print("\n⏳ Waiting for captcha to load...")
        time.sleep(5)

        # Extract captcha parameters
        print("\n" + "=" * 70)
        print("CAPTCHA ANALYSIS")
        print("=" * 70)

        # Method 1: From network logs
        print("\n🌐 Checking network logs...")
        network_params = extract_captcha_params_from_network()
        print(f"Network params: {json.dumps(network_params, indent=2)}")

        # Method 2: From page
        print("\n📄 Checking page...")
        page_params = extract_captcha_from_page()

        # For now, use manual solving
        print("\n" + "=" * 70)
        print("SOLVING CAPTCHA")
        print("=" * 70)

        if solve_nc_captcha_manual():
            print("\n✅ Captcha solved!")

            # Wait a bit
            time.sleep(3)

            # Now input OTP
            print("\n📱 Ready to input OTP")
            input_otp()

            print("\n🎉 Process completed!")
        else:
            print("\n❌ Failed to solve captcha")

        print("\nPress Enter to close...")
        input()

    except Exception as e:
        print(f"❌ Error in signup test: {e}")
        import traceback
        traceback.print_exc()
    finally:
        driver.quit()


def input_phone_num():
    phone_num = input("📱 Enter your phone number: ")
    phone_input = driver.find_element(
        By.XPATH,
        "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter your phone number']"
    )
    phone_input.send_keys(phone_num)
    print(f"✅ Entered phone: {phone_num}")


def input_otp():
    otp = input("🔐 Enter the OTP sent to your phone: ")
    try:
        otp_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//input[@placeholder='Please enter the OTP' or contains(@placeholder, 'OTP')]"
            ))
        )
        otp_input.send_keys(otp)
        print(f"✅ Entered OTP: {otp}")

        # Try to find and click submit button
        time.sleep(1)
        try:
            submit_btn = driver.find_element(By.XPATH,
                                             "//button[contains(text(), 'Verify') or contains(text(), 'Submit') or contains(@class, 'submit')]")
            submit_btn.click()
            print("✅ Clicked submit button")
        except:
            print("⚠️ Could not find submit button, you may need to click it manually")

    except Exception as e:
        print(f"❌ Error entering OTP: {e}")