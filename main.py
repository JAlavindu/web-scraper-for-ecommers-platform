import os
import time
from dotenv import load_dotenv
from google_signup import signup_with_google
from click_signup import click_signup_button
from login_with_google import google_login
import open_daraz

load_dotenv()
ANTI_API_KEY = os.getenv("ANTI_API_KEY")

def choosing_login_or_signup():
    choice = input("Do you want to (1) Sign Up or (2) Log In? Enter 1 or 2: ")
    if choice == '1':
        click_signup_button(open_daraz.driver)
        time.sleep(5)
        signup_with_google(open_daraz.driver)
    elif choice == '2':
        google_login(open_daraz.driver, ANTI_API_KEY)
        time.sleep(60)
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    open_daraz.daraz_open()
    choosing_login_or_signup()
    time.sleep(10)
    open_daraz.driver.quit()



