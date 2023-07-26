import os

import cv2
import pandas as pd
import streamlit as st
from PIL import Image


def display_video():
    video_path = os.path.join(os.getcwd(), "src/upload/video.mp4")
    csv_file_path = os.path.join(os.getcwd(), "src/upload/csv_file.csv")

    cap = cv2.VideoCapture("E:/AllProject/drontrackfrontend/src/upload/video.mp4")
    data = pd.read_csv("E:/AllProject/drontrackfrontend/src/upload/csv_file.csv")
    ret, frame = cap.read()
    st.write(data)

    frame_counter = 0
    outputs ={"predictions":[]}
    try:
        while ret:
            #st.image(frame)
            condition = data["Frame"] == frame_counter+1
            data_by_frame = data.loc[condition]
            for index, row in data_by_frame.iterrows():
                output = {
                    'x': row['X1'],
                    'y': row['Y1'],
                    'w': row['X2'],
                    'h': row['Y2'],
                    'confidence':row['Score'],
                    'class': "drone"
                }
                outputs["predictions"].append(output)
                st.write(outputs)
            ret, frame = cap.read()

            frame_counter += 1

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    display_video()