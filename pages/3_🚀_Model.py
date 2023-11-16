import io
import os
import tempfile
from io import BytesIO

import numpy as np
import pandas as pd

#import cv2
import requests
import streamlit as st
from PIL import Image

from src.config import image_path
from src.utils.upload import send_file, download_video_from_url
from src.utils.utils import save_csv_file


is_run = True
image_input = Image.new("RGB", (500, 500))# Get image detect
outputs = {} #To get detection coordonnate
nbr = 0 #Number of object detecting
img_url = ""
video_url = ""
is_video = False
video_path = ""
error_message = "Something is rong"
csv_file_url = ""

with st.sidebar:
    st.sidebar.image(Image.open(os.path.join(os.getcwd(), "src/testdata/13.jpg")), use_column_width=True, width=st.sidebar.width)

with open(os.path.join(os.getcwd(), "styles/style1.css")) as css_source:
    st.markdown(f"<style>{css_source.read()}</style>", unsafe_allow_html=True)

frame1, frame2, frame3 = st.columns([2, 3, 2])
# Frame1
with frame1:
    st.markdown("<h5 style='text-align:center;'>SAMPLES FROM TEST SET</h5>", unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(os.path.join(os.getcwd(), "src/testdata/2.jpg")), use_column_width=True,)
        with col2:
            st.image(Image.open(os.path.join(os.getcwd(), "src/testdata/5.jpg")), use_column_width=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(os.path.join(os.getcwd(), "src/testdata/3.jpg")), use_column_width=True)
        with col2:
            st.image(Image.open(os.path.join(os.getcwd(), "src/testdata/4.jpeg")), use_column_width=True)

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
                st.session_state["image_path"] = ""
                try:
                    if uploaded_file.name.endswith("mp4"):
                        is_video = True
                        # Write the file to a temporary location to read with OpenCV
                        with open("temp.mp4", "wb") as f:
                            f.write(uploaded_file.getbuffer())

                        cap = cv2.VideoCapture("temp.mp4")
                        ret, frame = cap.read()
                        while ret:
                            image = Image.fromarray(frame)
                            responses = send_file(image.tobytes())
                            if responses is None:
                                error_message = "No drone detect in your file "
                            else:
                                outputs = responses["coordinates"]
                                nbr = responses["num_objects"]
                                img_url = responses["image"]
                                #img_url = img_url.replace("http://13.48.57.180/","http://127.0.0.1:5000/")

                    else:
                        is_video = False

                        responses = send_file(uploaded_file)
                        if responses is None:
                            error_message = "No drone detect in your file "
                        else:
                            outputs = responses["coordinates"]
                            nbr = responses["num_objects"]
                            img_url = responses["image"]
                            img_url = img_url.replace("http://127.0.0.1:5000/", "http://13.48.57.180/")
                except Exception as e:
                    error_message = "No drone detect in your file "
            else:
                if st.session_state["image_path"] != "":
                    #image = Image.open(st.session_state["image_path"])
                    #image_bytes = io.BytesIO()
                    #image.save(image_bytes, format="PNG")

                    pil_image = Image.open(st.session_state["image_path"]).convert("L")
                    image_array = np.array(pil_image, "uint8")
                    data = {'image_data': image_array.tolist()}
                    response = requests.post('http://127.0.0.1:5000/process_image', json=data)

                    if response is None or response.status_code == 500:
                        error_message = "No drone detect in your file "
                    else:
                        data = response.json()
                        outputs = data["coordinates"]
                        nbr = data["num_objects"]
                        img_url = data["image"]
                        print("elooooooooooooooooooooooooo")
                        print(img_url)
                        #img_url = img_url.replace("http://127.0.0.1:5000/", "http://13.48.57.180/")



        #Dispplay image detecting in second frame
        # Column 2
with frame2:
    #if is_video:
            # Set the width and height of the div
        #div_width = 500
        #div_height = 500

    #else:
    if img_url == "":
        if st.session_state["image_path"] == os.path.join(os.getcwd(), "src/testdata/11.png"):
            st.image(Image.open(st.session_state["image_path"]), use_column_width=True, width=100)
            #st.write(error_message)
    else:
        print(img_url)
        response = requests.get(img_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        st.image(image, use_column_width=True,)
    with st.container():
        lambda_function = lambda x: 's' if x > 1 else ''
        st.write(f"{nbr} drone{lambda_function(nbr)} detecté{lambda_function(nbr)}")

    #Display  image detect coordonnate
    # Column 3
with frame3:
        # Affichage des données scrollables dans la colonne
    with st.expander("Drone coordinates"):

        st.write(outputs)
