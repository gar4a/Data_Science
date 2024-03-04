from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # This opens Chrome in fullscreen mode
chrome_options.add_experimental_option('detach', True)

# Set up the webdriver with the configured options
driver = webdriver.Chrome(options=chrome_options)
# Navigate to the website
url = 'https://www.data.gouv.fr/fr/'
driver.get(url)

# Wait for up to 3 seconds
time.sleep(3)
# Locate and click on the 'Données' link
try:
    donnees_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//li[contains(.,"Données")]'))
    )
    donnees_container.click()
    
    # Wait for up to 3 seconds
    time.sleep(3)
    # Find the input field and type the text
    search_input = driver.find_element(By.ID, 'search-input-1')
    search_input.send_keys("accidents corporels", Keys.RETURN)

    # Locate and click on the 'Bases de données annuelles des accidents' link
    element = driver.find_element(By.CLASS_NAME, "search-results")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    donnees_container_BD = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//li[contains(.,"Bases de données annuelles des accidents corporels de la circulation routière - Années de 2005 à 2022")]'))
    )
    donnees_container_BD.click()
    time.sleep(5)
    element = driver.find_element(By.ID, "resources-panel")
    driver.execute_script("arguments[0].scrollIntoView();", element)


    # **************************************** Find Data 2022 *************************************************
    # Find usagers-2022.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/62c20524-d442-46f5-bfd8-982c59763ec8"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find vehicules-2022.csv and click the download link

    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/c9742921-4427-41e5-81bc-f13af8bc31a0"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find lieux-2022.csv and click the download link

    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/a6ef711a-1f03-44cb-921a-0ce8ec975995"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find carcteristiques-2022.csv and click the download link

    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/5fc299c0-4598-4c29-b74c-6a67b0cc27e7"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # **************************************** Find Data 2021 *************************************************
    # Find usagers-2021.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/ba5a1956-7e82-41b7-a602-89d7dd484d7a"]')
    download_link.click()

    # Wait for up to 10 seconds
    time.sleep(10)
    # **************************************** Page 2
    download_link = driver.find_element(By.XPATH, '//a[@title="Page 2"]')
    download_link.click()
    # Wait for up to 15 seconds
    time.sleep(15)

    # Find vehicules-2021.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/0bb5953a-25d8-46f8-8c25-b5c2f5ba905e"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find lieux-2021.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/8a4935aa-38cd-43af-bf10-0209d6d17434"]')
    download_link.click()

    # Wait for up to 10 seconds
    time.sleep(10)
    # Find carcteristiques-2021.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/85cfdc0c-23e4-4674-9bcd-79a970d7269b"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # **************************************** Page 5
    download_link = driver.find_element(By.XPATH, '//a[@title="Page 5"]')
    download_link.click()
    # Wait for up to 5 seconds
    time.sleep(5)

    # **************************************** Find Data 2020 *************************************************
    # Find usagers-2020.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/78c45763-d170-4d51-a881-e3147802d7ee"]')
    download_link.click()

    # Wait for up to 10 seconds
    time.sleep(10)
    # Find vehicules-2020.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/a66be22f-c346-49af-b196-71df24702250"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find lieux-2020.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/e85c41f7-d4ea-4faf-877f-ab69a620ce21"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find carcteristiques-2021.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/07a88205-83c1-4123-a993-cba5331e8ae0"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # **************************************** Find Data 2019 *************************************************
    # Find usagers-2019.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/36b1b7b3-84b4-4901-9163-59ae8a9e3028"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find vehicules-2019.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/780cd335-5048-4bd6-a841-105b44eb2667"]')
    download_link.click()

    # **************************************** Page 6
    download_link = driver.find_element(By.XPATH, '//a[@title="Page 6"]')
    download_link.click()
    # Wait for up to 5 seconds
    time.sleep(5)

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find lieux-2019.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/2ad65965-36a1-4452-9c08-61a6c874e3e6"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find carcteristiques-2019.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/e22ba475-45a3-46ac-a0f7-9ca9ed1e283a"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # **************************************** Find Data 2018 *************************************************
    # Find usagers-2018.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/72b251e1-d5e1-4c46-a1c2-c65f1b26549a"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find vehicules-2018.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/b4aaeede-1a80-4d76-8f97-543dad479167"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find lieux-2018.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/d9d65ca1-16a3-4ea3-b7c8-2412c92b69d9"]')
    download_link.click()

    # **************************************** Page 7
    download_link = driver.find_element(By.XPATH, '//a[@title="Page 7"]')
    download_link.click()
    # Wait for up to 5 seconds
    time.sleep(5)

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find carcteristiques-2018.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/6eee0852-cbd7-447e-bd70-37c433029405"]')
    download_link.click()

# **************************************** Find Data 2017 *************************************************
    # Find usagers-2017.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/07bfe612-0ad9-48ef-92d3-f5466f8465fe"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find vehicules-2017.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/d6103d0c-6db5-466f-b724-91cbea521533"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find lieux-2017.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/9b76a7b6-3eef-4864-b2da-1834417e305c"]')
    download_link.click()

    # Wait for up to 5 seconds
    time.sleep(5)
    # Find carcteristiques-2017.csv and click the download link
    download_link = driver.find_element(By.XPATH, '//a[@href="https://www.data.gouv.fr/fr/datasets/r/9a7d408b-dd72-4959-ae7d-c854ec505354"]')
    download_link.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Wait for up to 60 seconds
    time.sleep(60)
    if 'driver' in locals():
        driver.quit()