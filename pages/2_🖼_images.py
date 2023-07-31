import os

import  streamlit as st
from PIL import Image

st.set_page_config(
page_title="Multipage App",
    page_icon="👋",
layout="wide",
)


test_data_dir = os.path.join(os.getcwd(), "src/testdata")
if "image_path" not in st.session_state:
    st.session_state["image_path"] = ""
with st.sidebar:
    st.sidebar.image(Image.open(os.path.join(os.getcwd(), "src/testdata/13.jpg")), use_column_width=True, width=st.sidebar.width)

with open(os.path.join(os.getcwd(), "styles/style1.css")) as css_source:
    st.markdown(f"<style>{css_source.read()}</style>", unsafe_allow_html=True)

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
            for i, image_path in enumerate(list_image):
                img = Image.open(image_path)
                img_resized = img.resize(image_size)
                # Afficher l'image redimensionnée dans la colonne correspondante
                col = columns[i % 8]
                col.image(img_resized, use_column_width=True)
                image_name = os.path.basename(image_path)
                button_label = f"Used {image_name}"
                if col.button(button_label):
                    # Lorsque le bouton est cliqué, définir l'image_path et rediriger vers la page "model"
                    st.session_state["image_path"] = image_path
                    st.experimental_rerun()
