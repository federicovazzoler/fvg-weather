import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# FIXME #1
# Download a WebDriver (e.g., ChromeDriver) that matches your browser version 
#from https://sites.google.com/a/chromium.org/chromedriver/downloads and place it 
# in a directory included in your system's PATH.

# Set up the WebDriver (this example uses Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (without opening a browser window)
driver = webdriver.Chrome(options=options)

# Go to the target website
driver.get('https://www.osmer.fvg.it/archivio.php?ln=&p=dati')

# Wait for the page to load completely
time.sleep(5)

# Locate the form fields and buttons
# This part will vary based on the actual HTML structure of the page
# Below is a generic approach

# Find the date fields (assuming there are input fields with specific IDs or classes)
start_date = driver.find_element(By.ID, 'startDateId')  # Update the ID
end_date = driver.find_element(By.ID, 'endDateId')  # Update the ID

# Enter the dates
start_date.clear()
start_date.send_keys('2023-01-01')  # Example start date
end_date.clear()
end_date.send_keys('2023-01-31')  # Example end date

# Find the search button and click it
search_button = driver.find_element(By.ID, 'searchButtonId')  # Update the ID
search_button.click()

# Wait for search results to load
time.sleep(5)

# Find the download button(s) and click to download CSV file(s)
download_buttons = driver.find_elements(By.CLASS_NAME, 'downloadButtonClass')  # Update the class name
for button in download_buttons:
    button.click()
    time.sleep(3)  # Wait for the download to complete

# Close the browser
driver.quit()
