import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.ins.tn/statistiques/117?fbclid=IwAR2YmzLrW7fPFUob33gKstmlxotMRGwcw_ueiRlmIjHty5SE_QCuSrX0yXc"

# Send a request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find elements containing specific data-target attribute
    data_target_values_of_interest = ["#2", "#3", "#4"]  # Update with actual values

    for data_target_value in data_target_values_of_interest:
        # Locate the element with the specific data-target attribute
        element = soup.find('a', {'data-target': data_target_value, 'class': 'btn btn-link'})

        if element:
            # Navigate to the parent table of the current element
            table = element.find_next('table')

            if table:
                # Extract data from the table
                table_data = []
                for row in table.find_all('tr'):
                    row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                    table_data.append(row_data)

                # Write table data to CSV file
                title = element.get_text(strip=True)
                csv_filename = f'{title}.csv'
                with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(table_data)

                print(f'Data for "{title}" table has been saved to {csv_filename}')
            else:
                print(f'Table not found for element with data-target "{data_target_value}"')
        else:
            print(f'Element with data-target "{data_target_value}" not found on the page.')
else:
    print(f"Error: Unable to retrieve the page (Status Code: {response.status_code})")
