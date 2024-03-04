import requests
import os

api_endpoint = 'https://www.data.gouv.fr/api/2/datasets/53698f4ca3a729239d2036df/resources/?page=1&type=main&page_size=999&q='
response = requests.get(api_endpoint)

dataToDownload = ['vehicules', 'lieux', 'usagers', 'caracteristiques']
basePath = 'C:/Esprit/dataScienceProject/webscrapping/'

if response.status_code == 200:
    data = response.json()
    for fileData in dataToDownload:
        download_folder = basePath + fileData + "/"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        for element in data['data']:
            if 'url' in element and fileData in element['url']:
                file_url = element['url']

                file_response = requests.get(file_url)

                if file_response.status_code == 200:
                    filename = os.path.basename(file_url)

                    file_path = os.path.join(download_folder, filename)

                    with open(file_path, 'wb') as file:
                        file.write(file_response.content)

                    print(f"File '{filename}' downloaded successfully to '{download_folder}'.")
                else:
                    print(f"Failed to download file from {file_url}. Status code: {file_response.status_code}")
else:
    print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
