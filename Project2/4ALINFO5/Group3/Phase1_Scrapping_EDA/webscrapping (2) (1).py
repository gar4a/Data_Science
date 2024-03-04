from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
import time

url = "https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/explore/query/SELECT%0A%20%20%60crash_date%60%2C%0A%20%20%60crash_time%60%2C%0A%20%20%60borough%60%2C%0A%20%20%60zip_code%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60location%60%2C%0A%20%20%60on_street_name%60%2C%0A%20%20%60off_street_name%60%2C%0A%20%20%60cross_street_name%60%2C%0A%20%20%60number_of_persons_injured%60%2C%0A%20%20%60number_of_persons_killed%60%2C%0A%20%20%60number_of_pedestrians_injured%60%2C%0A%20%20%60number_of_pedestrians_killed%60%2C%0A%20%20%60number_of_cyclist_injured%60%2C%0A%20%20%60number_of_cyclist_killed%60%2C%0A%20%20%60number_of_motorist_injured%60%2C%0A%20%20%60number_of_motorist_killed%60%2C%0A%20%20%60contributing_factor_vehicle_1%60%2C%0A%20%20%60contributing_factor_vehicle_2%60%2C%0A%20%20%60contributing_factor_vehicle_3%60%2C%0A%20%20%60contributing_factor_vehicle_4%60%2C%0A%20%20%60contributing_factor_vehicle_5%60%2C%0A%20%20%60collision_id%60%2C%0A%20%20%60vehicle_type_code1%60%2C%0A%20%20%60vehicle_type_code2%60%2C%0A%20%20%60vehicle_type_code_3%60%2C%0A%20%20%60vehicle_type_code_4%60%2C%0A%20%20%60vehicle_type_code_5%60/page/filter"

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

try:
    driver.get(url)
    driver.implicitly_wait(10)

    # Wait for the table with the specified class to be present
    table_locator = (By.TAG_NAME, 'table')
    table = WebDriverWait(driver, 20).until(EC.presence_of_element_located(table_locator))

    if table:
        result_df = pd.DataFrame()
        total_pages = 260 000

        for page in range(1, total_pages + 1):
            next_button_locator = (By.CSS_SELECTOR, 'a.next-link')
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(next_button_locator))
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(10)


            table = WebDriverWait(driver, 10).until(EC.presence_of_element_located(table_locator))
            table_html = table.get_attribute('outerHTML')

            # Use BeautifulSoup to extract table data
            soup = BeautifulSoup(table_html, 'html.parser')
            table_data = []

            # Check if table has 'th' (header) and 'td' (data) elements
            if soup.find('th') and soup.find('td'):
                #th = ag-header-cell-comp-wrapper
                for row in soup.find_all('tr'):
                    row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                    table_data.append(row_data)

                # Check if table_data has rows
                if table_data:
                    # Convert table data to DataFrame
                    df = pd.DataFrame(table_data[1:], columns=table_data[0])
                    result_df = pd.concat([result_df, df], ignore_index=True)
                    print(result_df.head())
                else:
                    print(f"No data found on page {page}")
            else:
                print(f"No 'th' (header) or 'td' (data) elements found on page {page}")

        result_df.to_excel("nyc_collisions_data_all_pages100K.xlsx", index=False)
        print("Data successfully exported")
    else:
        print("No table")
finally:
    driver.quit()
