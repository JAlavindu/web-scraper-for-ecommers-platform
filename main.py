import os
import time

import open_daraz
from google_signup import signup_with_google
from click_signup import click_signup_button
import open_daraz

ANTI_API_KEY = os.getenv("ANTI_API_KEY")

if __name__ == "__main__":
    open_daraz.daraz_open()
    click_signup_button(open_daraz.driver)
    time.sleep(5)
    signup_with_google(open_daraz.driver)


    open_daraz.driver.quit()



