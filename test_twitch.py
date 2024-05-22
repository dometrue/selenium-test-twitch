# Import necessary libraries from selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Setting up Chrome options to emulate an iPhone X for mobile web testing
opts = Options()
opts.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})

# Specifying the path to the ChromeDriver and setting up the driver
service = Service(r'C:\Users\vlad_\Desktop\ChromeDriver\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=opts)

try:
    # Navigate to Twitch mobile site
    driver.get('https://m.twitch.tv/')
    # Wait for the body of the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print("Page loaded.")

    try:
        # Click the cookies acceptance button if it appears
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.ScReactModalBase-sc-26ijes-0.eViShK.tw-modal-layer > div > div > div:nth-child(2) > div > div > div.Layout-sc-1xcs6mc-0.gfNyDl > button"))).click()
        print("Cookies accepted.")
    except TimeoutException:
        print("No cookie pop-up appeared.")

    # Click on the search icon
    search_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > nav > div.Layout-sc-1xcs6mc-0.hSqeuh > a")))
    search_icon.click()
    print("Search icon clicked.")

    # Enter "StarCraft II" in the search box and submit
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="search"]')))
    search_box.send_keys('StarCraft II', Keys.ENTER)
    print("Search term entered.")

    # Wait for the page to load search results
    time.sleep(2)
#Issue with the header which prevents scrolling
#Potential dynamic content loading issues

    # Define the CSS selector for the target element (which we want to hover on)
    css_selector = "#__next > div > main > div > div > section:nth-child(3) > div.Layout-sc-1xcs6mc-0.ftRjUA > a > p"

    # Wait until the element is present in the DOM
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

    # Scroll to the element using JavaScript
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(2)  # Wait for the scroll to complete

    # Use ActionChains to move to the element and hover over it
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)  # Allow some time to observe the hover action

    # Perform a scroll action to ensure full scroll functionality
    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)

    # Verify the scroll position
    current_position = driver.execute_script("return window.pageYOffset;")
    print("Current Scroll Position:", current_position)

    # Action on the streamer link
    print("Looking for the streamer link...")
    streamer = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > main > div > div > section:nth-child(4) > div:nth-child(2) > a > div > div.Layout-sc-1xcs6mc-0.jZqEZt > h4")))
    streamer.click()
    print("Streamer link found and clicked.")

    # Wait for the streamer page to load and take a screenshot
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div > main > div > section.sc-8582c84-1.hpIzNt > div > div > div > video")))

    # Delay for page elements to stabilize before taking a screenshot

    time.sleep(5)

    driver.save_screenshot('streamer_page.png')
    print("Screenshot taken.")

finally:
    # Ensure the driver quits regardless of previous errors
    driver.quit()

print("Test completed.")
