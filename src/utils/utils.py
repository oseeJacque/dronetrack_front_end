import os

import requests
def save_csv_file(url,save_path):

    response = requests.get(url)
    if requests.status_codes == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print("CSV file saved successfully.")
        return True
    else:
        print(f"Failed to retrieve the CSV data. Status Code: {response.status_code}")
        return False