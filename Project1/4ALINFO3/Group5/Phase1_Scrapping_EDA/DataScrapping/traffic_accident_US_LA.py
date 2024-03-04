import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def is_file_downloaded(download_dir, file_name):
    return os.path.exists(os.path.join(download_dir, file_name))

def download_csv_with_selenium():
    # Get the current directory
    download_dir = os.getcwd()

    # Set Chrome options to specify the download directory
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Using ChromeDriverManager to automatically download and set up ChromeDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    try:
        # URL of the webpage to scrape
        url = "https://data.lacity.org/Public-Safety/Traffic-Collision-Data-from-2010-to-Present/d5tf-ez2w/about_data"

        # Navigate to the webpage
        driver.get(url)

        # Wait for the export button to be clickable
        export_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Export')]"))
        )

        # Click the export button
        export_button.click()

        # Wait for the export dialog to appear
        export_dialog = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'export-dataset-dialog'))
        )

        # Find and click the download button
        download_button = export_dialog.find_element_by_xpath("//button[@data-testid='export-download-button']")
        download_button.click()

        print("Download initiated...")

        # Measure the elapsed time until the element disappears
        start_time = time.time()
        WebDriverWait(driver, 70000).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'forge-toast__container--active')))
        elapsed_time = time.time() - start_time

        # Wait until the file is downloaded or until a timeout is reached
        file_name = "Traffic_Collision_Data_from_2010_to_Present_20240216.csv"
        timeout = 70000 - elapsed_time
        start_time = time.time()
        while time.time() - start_time < timeout:
            if is_file_downloaded(download_dir, file_name):
                print("Download completed!")
                break
            time.sleep(1)  # Check every 1 second
        else:
            print("Download timed out!")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    download_csv_with_selenium()
