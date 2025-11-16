from delay_humanlike import human_like_delay
from selenium.webdriver.common.by import By
from slider import solve_slider_human_like
from undetectable_driver import create_undetectable_driver

driver = create_undetectable_driver()

def solve_captcha():
    """Main captcha solving function"""
    try:
        print("\n🎯 Locating slider...")
        human_like_delay(2, 3)

        slider_element = None
        iframe_index = None

        # Check iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"📦 Found {len(iframes)} iframes")

        for idx, iframe in enumerate(iframes):
            try:
                driver.switch_to.frame(iframe)

                # Try multiple selectors
                selectors = [
                    ".nc_iconfont.btn_slide",
                    ".nc-lang-cnt",
                    "#nc_1_n1z",
                    "[id^='nc_'][id$='_n1z']",
                    ".btn_slide",
                    "[class*='btn_slide']",
                    ".slidetounlock"
                ]

                for selector in selectors:
                    try:
                        slider = driver.find_element(By.CSS_SELECTOR, selector)
                        iframe_index = idx
                        print(f"✅ Found slider in iframe {idx}: {selector}")
                        break
                    except:
                        continue

                if slider:
                    break
                else:
                    driver.switch_to.default_content()

            except Exception as e:
                driver.switch_to.default_content()
                continue

        if not slider_element:
            print("❌ Could not find slider")
            driver.switch_to.default_content()

            # Check for error/blocked message
            try:
                error_msg = driver.find_element(By.XPATH, "//*[contains(text(), 'unusual traffic')]")
                print("⚠️ DETECTED: Bot detection triggered!")
                print("💡 TIP: Try closing browser completely and running again")
                print("💡 TIP: Or wait a few minutes before retrying")
            except:
                pass

            return False

        # Attempt solve
        result = solve_slider_human_like(driver, slider_element)

        driver.switch_to.default_content()
        return result

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        driver.switch_to.default_content()
        return False