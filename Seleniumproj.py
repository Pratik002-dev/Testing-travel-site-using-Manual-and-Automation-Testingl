from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Function to automate the login process
def automate_login(phone_number, otp):
    driver = webdriver.Chrome()
    driver.get("your_website_url")

    # Test Case 1: Valid SignUp with Phone Number and OTP Verification
    # Enter valid phone number and submit
    phone_input = driver.find_element(By.TAG_NAME,"input")
    phone_input.send_keys(phone_number)
    submit_button = driver.find_element(By.TAG_NAME,"scroll")

    # Wait for OTP input field
    time.sleep(2)

    # Enter valid OTP and submit
    otp_input = driver.find_element(By.TAG_NAME,"input")
    otp_input.send_keys(otp)
    submit_button.click()

    # Test Case 2: Invalid Phone Number Format
    # Clear phone number input field
    phone_input.clear()
    # Enter invalid phone number format
    phone_input.send_keys("79780235")
    submit_button.click()
    # Handle validation message

    # Test Case 3: Invalid OTP Verification
    # Enter valid phone number
    phone_input.clear()
    phone_input.send_keys(phone_number)
    submit_button.click()
    time.sleep(2)
    # Enter invalid OTP
    otp_input.clear()
    otp_input.send_keys("invalid_otp")
    submit_button.click()
    # Handle validation message


    # Test Case 4: Session Timeout Handling for OTP
    # Simulate session timeout
    time.sleep(300)  # Assuming session timeout is 5 minutes (300 seconds)
    # Handle session timeout message

    driver.quit()  # Close the WebDriver session


# Sample test data for two users
user1_phone = "7978023538"
user1_otp = "4592"
user2_phone = "8338010201"
user2_otp = "7604"
# Automate login process for both users
automate_login(user1_phone, user1_otp)
automate_login(user2_phone, user2_otp)
