
import requests

def send_file(file):
    url = "http://127.0.0.1:5000/detect/upload"  # URL de l'API pour envoyer le fichier

    try:
        files = {'file': file}
        response = requests.post(url, files=files)  # Envoie la requête POST avec le contenu du fichier
        print(response.content)  # Vérifie si la requête a réussi
        return response.text  # Renvoie la réponse du serveur (si nécessaire)

    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'envoi du fichier :", e)
