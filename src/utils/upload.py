import cv2
import requests

def send_file(file):

    #http://13.48.57.180
    url = "http://127.0.0.1:5000/detect/upload"  # URL de l'API pour envoyer le fichier
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

def convert_frame_to_png(frame):
    _, encoded_frame = cv2.imencode(".png", frame)
    return encoded_frame.tobytes()
"""
        if not is_run:
            st.write(f"<div style='width: {div_width}px; height: {div_height}px;'>", unsafe_allow_html=True)
            if video_path == "":
                st.write(error_message)
            else:
                st.video(video_path)
                # Display coordonnate of object detect
                cap = cv2.VideoCapture(video_path)
                data = pd.read_csv(csv_file_url)
                ret, frame = cap.read()
                frame_counter = 0

                try:

                    while ret:
                        # st.image(frame)
                        condition = data["Frame"] == frame_counter + 1
                        data_by_frame = data.loc[condition]
                        for index, row in data_by_frame.iterrows():
                            output = {
                                'x': row['X1'],
                                'y': row['Y1'],
                                'w': row['X2'],
                                'h': row['Y2'],
                                'confidence': row['Score'],
                                'class': "drone"
                            }
                            print(output)
                            outputs["predictions"].append(output)
                            st.write(outputs)

                        ret, frame = cap.read()

                        frame_counter += 1

                    cap.release()
                    cv2.destroyAllWindows()
                    st.write("L'exécution terminée ") 

                except Exception as e:
                    print(e)
            st.write("</div>", unsafe_allow_html=True)
        else:
            st.balloons()
        """