import csv
import os
import time
import re
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

def scroll_into_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)

def click_element(driver, element):
    driver.execute_script("arguments[0].click();", element)

def clean_rows(df):
    """Handles rows with colspan in the CSS and Vorspalte class by removing them."""
    condition = (df.astype(str).apply(lambda x: x.str.contains("colspan", na=False)).any(axis=1)) \
                | (df.astype(str).apply(lambda x: x.str.contains("Vorspalte", na=False)).any(axis=1))
    
    cleaned_df = df.loc[~condition]
    return cleaned_df.dropna()  # Drop rows with any NaN values

def sanitize_filename(filename):
    """Replaces invalid characters in the filename."""
    invalid_chars = r'[/\\:*?"<>|]'
    return re.sub(invalid_chars, '_', filename)

def handle_cookie_consent(driver):
    try:
        # Wait for the cookie consent popup to appear
        cookie_popup = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "c-button.close.consentToAll.js-banner-button-consent-to-all"))
        )

        # Scroll into view and click "Consent to All"
        scroll_into_view(driver, cookie_popup)
        click_element(driver, cookie_popup)

    except Exception as e:
        print(f"Error handling cookie consent popup: {e}")

def scrape_and_export_table(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="wide")

    try:
        if not table:
            raise ValueError("Table not found on the page.")

        # Extracting data using BeautifulSoup
        data = []
        headers = [th.text.strip() for th in table.find("thead").find_all("th")]

        # Check if tbody is present, otherwise, return early
        tbody = table.find("tbody")
        if not tbody:
            raise ValueError("Table does not have a tbody element.")

        for row in tbody.find_all("tr"):
            data.append([td.text.strip() for td in row.find_all("td")])

        # Create the directory if it doesn't exist
        directory = os.path.expanduser("~/Documents/2CSV")
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Sanitize the filename
        filename = sanitize_filename(filename)

        # Create a CSV file
        filepath = os.path.join(directory, filename)
        with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            # Write the table headers
            writer.writerow(headers)

            # Write the cleaned table rows
            cleaned_data = clean_rows(pd.DataFrame(data, columns=headers))
            for row_data in cleaned_data.values:
                writer.writerow(row_data)

        print(f"Table data scraped and exported to {filepath}")

    except ValueError as ve:
        print(f"Skipping link. {ve}")

    except Exception as e:
        print(f"Error exporting data to CSV: {e}")

def main():
    # Set up Selenium WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Navigate to the main page
    driver.get("https://www.destatis.de/EN/Themes/Society-Environment/Traffic-Accidents/_node.html#sprg265458")

    # Handle cookie consent popup
    handle_cookie_consent(driver)

    # Check if there are any frames and switch to them if necessary
    frames = driver.find_elements(By.TAG_NAME, "iframe")
    if frames:
        driver.switch_to.frame(frames[0])  # Assuming the button is in the first frame

    # Find the toggle button and click it
    toggle_button = driver.find_element(By.XPATH, '//h3[@class="c-toggle__heading heading inactive-control"]/button[contains(text(), "Road traffic accidents")]')
    scroll_into_view(driver, toggle_button)
    click_element(driver, toggle_button)
    time.sleep(3)

    # Wait for the list of links to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "c-list__item")))

    # Find all links with class="c-list__item"
    links = driver.find_elements(By.CLASS_NAME, "c-list__item")
    print(links)

    for link in links:
        # Extract link information before clicking
        link_text = link.text
        link_url = link.get_attribute("href")

        # Find the anchor element within the list item and click it
        link_anchor = link.find_element(By.TAG_NAME, "a")
        time.sleep(3)
        scroll_into_view(driver, link_anchor)
        try:
            click_element(driver, link_anchor)
        except Exception as e:
            print(f"Error clicking the link: {e}")

        # Wait for the page to load
        time.sleep(3)

        # Get the URL of the current page (after clicking the link)
        current_url = driver.current_url
        print(current_url)

        # Define a filename based on the extracted link information
        filename = f"{link_text.lower().replace(' ', '_')}_data.csv"
        print(filename)

        # Scrape and export table from the current page
        scrape_and_export_table(current_url,  filename)


        # Go back to the main page
        driver.back()

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    main()
