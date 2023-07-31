import os

import streamlit as st
from PIL import Image

from src.config import image_path, test_data_dir, css_file

st.set_page_config(
page_title="Multipage App",
    page_icon="👋",
layout="wide"
)
test_data_dir = os.path.join(os.getcwd(), "src/testdata")
st.session_state["image_path"] = os.path.join(os.getcwd(), "src/testdata/11.png")
with st.sidebar:
    st.sidebar.image(Image.open(os.path.join(os.getcwd(), "src/testdata/13.jpg")), use_column_width=True, width=st.sidebar.width)

with open(os.path.join(os.getcwd(), "styles/style1.css")) as css_source:
    st.markdown(f"<style>{css_source.read()}</style>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([5, 2, 2])
button_style = "background-color: green; color: white;"

with col1:
    st.markdown("<h3 style='text-align:left;'>\t ☆ Drone_detect Computer Vision Project</h3>", unsafe_allow_html=True)

with col2:
    if st.button("📥Download this Dataset"):
        # Redirection vers la page 1
        st.experimental_rerun()

with col3:
    if st.button("🚀Try Pre-Trained Model"):
        # Redirection vers la page 2
        st.experimental_rerun()

st.divider()

frame1, frame2 = st.columns([5, 1])

with frame1:
    st.markdown('''
           <style>
               .custom-container {
                   background-color: black;
                   height: 130px;
                   border: 2px dashed white;
                   border-radius: 15px;
                   padding: 10px;
                   justify-content: center;
                   align-items: center;
                   position: relative;
                    overflow: hidden;
                   display: flex;
                   flex-direction: column;
                  justify-content: center;
                    color: white;
                transition: background-color 0.3s;
            }
            .custom-container:hover {
                background-color: #222; 
            }
            .text {
                text-align: center;
                margin: 10px 0;
            }
            .explore{
            text-align: right;
             margin: 10px 0;
            }
            .text_grid{
            color: #888888;
            }
               }
           </style>
       ''', unsafe_allow_html=True)

    # Utiliser la classe CSS pour appliquer le style au conteneur
    st.markdown(f'<div class="custom-container"><p> <strong style="font-size:20px;">TRY THIS MODEL</strong><br>Drop an image or<br><a class="text" href="http://localhost:8501/Model", style="color:green;">Browse your device</a></p></div>',
                unsafe_allow_html=True)


    st.divider()
    st.markdown('<p class = "text_grid">IMAGES</p>', unsafe_allow_html=True)

#Show image in interface
    if not os.path.exists(test_data_dir):
        st.error("Le répertoire 'testdata' n'existe pas.")
    else:
        list_image = [os.path.join(test_data_dir, filename) for filename in os.listdir(test_data_dir) if
                      filename.endswith(('jpg', 'jpeg', 'png'))]

        if len(list_image) == 0:
            st.warning("Aucune image trouvée dans le répertoire 'testdata'.")
        else:
            columns = st.columns(8)
            image_size = (200, 200)
            for i in range(8):
                img = Image.open(list_image[i])
                img_resized = img.resize(image_size)
                # Afficher l'image redimensionnée dans la colonne correspondante
                columns[i].image(img_resized, use_column_width=True)


    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class = "text_grid">987 images </p>', unsafe_allow_html=True)
    with col2:
        st.markdown('<a class="explore" href="#" style="color:green;"><h6>Explore Dataset >> </h6></a>', unsafe_allow_html=True)
    with st.container():
        pass

    st.divider()
    st.markdown('<h5>Trained Model API</h5>', unsafe_allow_html=True)
    st.markdown('<p>This project has a trained model available that you can  &nbsp <a class="text" href="#" style="color:green;">try in your browser </a> &nbsp and use to get predictions via our Hosted Inference API and other deployment methods.</p>',unsafe_allow_html=True)
    with st.container():
        pass
with frame2:
    st.markdown("<h6><u>SOURCE</u></h6>", unsafe_allow_html=True)
    st.write("Dr Bienvenue MOUTOUAMA")
    st.markdown("<h6><u>LAST UPDATED</u></h6>", unsafe_allow_html=True)
    st.write("07/2023")
    st.markdown("<h6><u>PROJECT TYPE</u></h6>", unsafe_allow_html=True)
    st.write("Computer vision")
    st.markdown("<h6><u>SUBJECT</u></h6>", unsafe_allow_html=True)
    st.write("Drone")
    st.divider()







