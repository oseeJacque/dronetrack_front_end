import io
import os

import cv2
import streamlit as st
from PIL import Image

from src.config import image_path
from src.utils.upload import send_file

is_run = True
image_input = Image.new("RGB", (500, 500))# Get image detect
outputs = {} #To get detection coordonnate
nbr = 0 #Number of object detecting
is_video = False
with st.sidebar:
    st.sidebar.image(Image.open(os.path.join(os.getcwd(), "src/testdata/13.jpg")), use_column_width=True, width=st.sidebar.width)

with open("E:/AllProject/AllProject/dronetrack/styles/style1.css") as css_source:
    st.markdown(f"<style>{css_source.read()}</style>", unsafe_allow_html=True)

frame1, frame2, frame3 = st.columns([2, 3, 2])
# Frame1
with frame1:
    st.markdown("<h5 style='text-align:center;'>SAMPLES FROM TEST SET</h5>", unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open("E:/AllProject/AllProject/dronetrack/src/testdata/2.jpg"), use_column_width=True,)
        with col2:
            st.image(Image.open("E:/AllProject/AllProject/dronetrack/src/testdata/5.jpg"), use_column_width=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open("E:/AllProject/AllProject/dronetrack/src/testdata/3.jpg"), use_column_width=True)
        with col2:
            st.image(Image.open("E:/AllProject/AllProject/dronetrack/src/testdata/4.jpeg"),
                         use_column_width=True)

        # Text button with yellow text

        if st.button(
                label="Visualize >>",
                key="button1",
                help="Visualize data set",
                on_click=None,
                args=None,
                kwargs=None,
        ):
            # Execute this code when w
            st.write("Button is pressed")

        # Diver to upload video or image
    st.divider()
    # Create another container with a title
    with st.container():
        with st.container():
            st.markdown("<h6 style='text-align:center;'>Drop image/Video file</h6>", unsafe_allow_html=True)
            st.write("<h6 style='text-align:center;color:##EEEEEE;'>or</h6>", unsafe_allow_html=True)
            st.write("<h6 style='text-align:center;'>Paste youtube / image url</h6>", unsafe_allow_html=True)
            # Input text to get the link
            link = st.text_input("", placeholder="Link")

            # Container to upload image or Vide
        with st.container():
            uploaded_file = st.file_uploader("Choose image or Video", type=["jpg", "jpeg", "png", "mp4"])
            if uploaded_file is not None:
                if uploaded_file.name.endswith("mp4"):
                    is_video = True
                    g = io.BytesIO(uploaded_file.read())

                    #Save videos on local
                    #with open(video_input_path, "wb") as video_file:
                            #video_file.write(g.read())

                    #is_run = tracking_drone_in_video()
                else:
                    is_video = False
                    if uploaded_file is not None:
                        send_file(uploaded_file.getvalue())
                    # Save image to path source
                    #image_input.save(image_path)

                    #Call detect drone in image fonction
                    #outputs, image_input, nbr = detect_drone_in_image(image_path)



        #Dispplay image detecting in second frame
        # Column 2
with frame2:
    if is_video:
            # Set the width and height of the div
        div_width = 500
        div_height = 500
        if not is_run:
            st.write(f"<div style='width: {div_width}px; height: {div_height}px;'>", unsafe_allow_html=True)
            #st.video(video_path)
            st.write("</div>", unsafe_allow_html=True)
        else:
            st.balloons()
    else:
        st.image(image_input, use_column_width=True, width=100)
        with st.container():
            lambda_function = lambda x: 's' if x > 1 else ''
            st.write(f"{nbr} drone{lambda_function(nbr)} detecté{lambda_function(nbr)}")

    #Display  image detect coordonnate
    # Column 3
with frame3:
        # Affichage des données scrollables dans la colonne
    with st.expander("Données scrollables"):

        st.write(outputs)


