from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from django.shortcuts import render


def home(request):
    if request.method == "POST":
        # Retrieve data from the form
        country = request.POST.get('country')
        star = request.POST.get('star')
        source = request.POST.get('source')
        url = request.POST.get('url')
        review_text = request.POST.get('review')
        email = request.POST.get('email')
        password = request.POST.get('password')

        login_trustpilot_with_google(email, password)

    return render(request, 'app/home.html')


def login_trustpilot_with_google(email, password):
    # Start the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open Trustpilot
        driver.get("https://www.trustpilot.com/")
        time.sleep(3)  # Allow time for page load

        # Click on "Log in" button
        login_button = driver.find_element(By.LINK_TEXT, "Log in")
        login_button.click()
        time.sleep(6)

        # Click on "Continue with Google"
        google_login_button = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[1]/div/div/div/div[1]')
        google_login_button.click()
        time.sleep(5)

        # Switch to Google login window
        # Switch to the new Google login window
        driver.switch_to.window(driver.window_handles[1])

        # Input email
        email_input = driver.find_element(By.ID, "identifierId")
        email_input.send_keys(email)
        driver.find_element(By.ID, "identifierNext").click()
        time.sleep(3)

        # Input password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        driver.find_element(By.ID, "passwordNext").click()
        time.sleep(5)

        # Switch back to Trustpilot window if needed
        driver.switch_to.window(driver.window_handles[0])
        print("Logged in successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the driver after the process
        driver.quit()
