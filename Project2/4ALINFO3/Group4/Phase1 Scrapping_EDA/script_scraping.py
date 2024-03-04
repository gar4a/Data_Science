#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
import pandas as pd
import time
#ETAPE1
def initialize_driver():
    options = Options()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)
#ETAPE2
def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def click_and_retry(driver, element, locator, retry_attempts=3):
    for _ in range(retry_attempts):
        try:
            element.click()
            return True
        except StaleElementReferenceException:
            print("Stale Element Reference Exception. Retrying...")
            element = wait_for_element(driver, locator)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
    return False
# ETAPE 3
def scrape_table_data(driver, table_locator):
    table = wait_for_element(driver, table_locator)
    table_html = table.get_attribute('outerHTML')
    soup = BeautifulSoup(table_html, 'html.parser')
    html_table = soup.find('table')
    return pd.read_html(str(html_table))[0]

def main():
    url = "https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95"
    driver = initialize_driver()

    try:
        driver.get(url)
        driver.implicitly_wait(10)

        # Wait for the table with the specified class to be present
        table_locator = (By.CLASS_NAME, 'socrata-table.frozen-columns')

        if not (table := wait_for_element(driver, table_locator)):
            print("No table with class 'socrata-table frozen-columns' found on the page.")
            return

        # Initialize an empty list to store the DataFrames
        dfs = []

        # Find the total number of pages
        total_pages = 500

        # Iterate through each page and append data to the DataFrames list
        for page in range(1, total_pages + 1):
            # Wait for the next page button to be clickable
            next_button_locator = (By.XPATH, "//button[@class='pager-button-next']")
            next_button = wait_for_element(driver, next_button_locator)

            # Click on the next page button using JavaScript
            if not click_and_retry(driver, next_button, next_button_locator):
                print("Failed to click next button. Exiting.")
                break

            time.sleep(2)  # You can adjust the sleep time as needed

            # Re-locate the table after it becomes stale
            df = scrape_table_data(driver, table_locator)

            # Display the first few rows of the result DataFrame
            print(df.head())

            # Concatenate DataFrames using pandas.concat
            dfs.append(df)

        # Concatenate all DataFrames
        result_df = pd.concat(dfs, ignore_index=True)
#ETAPE 5 NETTOYAGE 
        # Remove columns with all null values
        result_df = result_df.dropna(axis=1, how='all')
#Étape 6 
        # Export the cleaned result DataFrame to an Excel file
        result_df.to_excel("DataCollisions.xlsx", index=False)
        print("Cleaned data successfully exported .xlsx")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

