
import requests

def send_file(file):
    url = "http://13.48.57.180/detect/upload"  # URL de l'API pour envoyer le fichier
    try:
        files = {'file': file}
        response = requests.post(url, files=files)  # Envoie la requête POST avec le contenu du fichier
        return response.json()  # Renvoie la réponse du serveur (si nécessaire)

    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'envoi du fichier :", e)


def download_video_from_url(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
            return True
        print(f"La vidéo a été téléchargée avec succès : {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Une erreur est survenue lors du téléchargement : {e}")
        return False