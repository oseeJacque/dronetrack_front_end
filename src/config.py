from PIL import Image
import os
current_file = os.path.abspath(__file__)
global base_dir

base_dir = os.path.dirname(current_file)

css_file = os.path.join(os.getcwd(), "pages")
test_data_dir = os.path.join(os.getcwd(), "testdata")
image_path = os.path.join(test_data_dir, "13.jpg")

print(test_data_dir)

