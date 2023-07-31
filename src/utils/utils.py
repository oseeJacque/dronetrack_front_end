import os
from io import BytesIO

import requests
from PIL import Image


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

def compress_image_lossless(input_path):
    try:
        # Ouvrir l'image avec PIL
        image = Image.open(input_path)

        # Enregistrer l'image compressée sans perte dans une mémoire temporaire (BytesIO)
        temp_buffer = BytesIO()
        image.save(temp_buffer, format="PNG")

        print("Image compressée sans perte avec succès.")

        # Rembobiner le tampon pour la lecture ultérieure
        temp_buffer.seek(0)

        # Retourner l'objet Image compressé sans enregistrer l'image sur le disque
        return Image.open(temp_buffer)

    except Exception as e:
        print("Une erreur est survenue lors de la compression de l'image :", str(e))
        return None