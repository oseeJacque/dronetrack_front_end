import streamlit as st
from PIL import Image


def frame1_1():
    st.markdown("**ÉCHANTILLONS DES DONNÉES**", unsafe_allow_html=True)    # Create a container with a title
    # Define CSS style for the image grid
    st.markdown(
        """
        <style>
        .image-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.image(Image.open("E:/AllProject/AllProject/trackingdrone/src/testdata/2.jpg"), use_column_width=True, width=100)
        with col2:
            st.image(Image.open("E:/AllProject/AllProject/trackingdrone/src/testdata/5.jpg"), use_column_width=True)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open("E:/AllProject/AllProject/trackingdrone/src/testdata/3.jpg"), use_column_width=True)
        with col2:
            st.image(Image.open("E:/AllProject/AllProject/trackingdrone/src/testdata/4.jpeg"), use_column_width=True)

        # Text button with yellow text

        st.write("<div style='display: flex; justify-content: center;'>",unsafe_allow_html=True)
        if st.button(
                label="Visualiser >>",
                key="button1",
                help="visualiser l'ensemble des données de test",
                on_click=None,
                args=None,
                kwargs=None,
        ):
            # Code à exécuter lorsque le bouton est cliqué
            st.write("Le bouton a été cliqué!")
        st.write("</div>",unsafe_allow_html=True)

        #Diver to upload video or image

    st.divider()
    # Create another container with a title
    with st.container():
        st.markdown("***Déposer une image/fichier vidéo***", unsafe_allow_html=True)
        st.write("ou")
        st.write("Coller YouTube / URL de l'image")
        #Input text to get the link
        link = st.text_input("", placeholder="Link")

    #Container to upload image or video
    with st.container():
        uploaded_file = st.file_uploader("Choisir une image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            st.image(img, use_column_width=True, width=100)

    with st.container():
        uploaded_video = st.file_uploader("Choisir une vidéo", type=["mp4"], accept_multiple_files=False)

