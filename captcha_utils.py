import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_captcha(driver, api_key=None):
    """
    Checks for CAPTCHA and attempts to solve it or prompts user.
    """
    try:
        # Check for common CAPTCHA indicators
        captcha_indicators = [
            "//iframe[contains(@src, 'recaptcha')]",
            "//div[contains(text(), 'Verify it')]",
            "//div[@id='captcha-form']"
        ]
        
        found_captcha = False
        for xpath in captcha_indicators:
            if driver.find_elements(By.XPATH, xpath):
                found_captcha = True
                break
        
        if not found_captcha:
            return # No CAPTCHA detected

        print("⚠️ CAPTCHA detected!")
        
        if api_key:
            try:
                from twocaptcha import TwoCaptcha
                solver = TwoCaptcha(api_key)
                print("Attempting to solve with 2Captcha...")
                
                # Try to find sitekey
                sitekey = None
                match = re.search(r'data-sitekey=["\'](.+?)["\']', driver.page_source)
                if match:
                    sitekey = match.group(1)
                
                if not sitekey:
                    iframes = driver.find_elements(By.TAG_NAME, "iframe")
                    for iframe in iframes:
                        src = iframe.get_attribute("src")
                        if src and "recaptcha" in src:
                            match = re.search(r'k=([^&]+)', src)
                            if match:
                                sitekey = match.group(1)
                                break
                
                if sitekey:
                    print(f"Found sitekey: {sitekey}")
                    result = solver.recaptcha(sitekey=sitekey, url=driver.current_url)
                    code = result['code']
                    print("✅ CAPTCHA solved by service!")
                    
                    # Inject response
                    driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML = "{code}";')
                    
                    # Try to submit form or call callback (this is tricky and site-specific)
                    # For Google, sometimes just injecting isn't enough.
                    # We'll try to find a callback or just let the user proceed.
                    print("Response injected. You may need to click 'Next' or 'Verify'.")
                    
                else:
                    print("❌ Could not find sitekey for automated solving.")
            except ImportError:
                print("❌ 2captcha-python library not installed.")
            except Exception as e:
                print(f"❌ Error during automated solving: {e}")

        # Fallback to manual
        print("\n" + "="*50)
        print("🚨 MANUAL INTERVENTION REQUIRED 🚨")
        print("Please solve the CAPTCHA manually in the browser.")
        print("Once solved and you are on the next screen, press Enter here to continue...")
        print("="*50)
        input()
        print("Resuming script...")
        
    except Exception as e:
        print(f"Error in CAPTCHA handler: {e}")
        import traceback
        traceback.print_exc()
        # If connection is lost, re-raise to stop the script
        if "Connection aborted" in str(e) or "invalid session" in str(e):
            raise
