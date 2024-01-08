import streamlit as st
import cv2
import numpy as np
from filter_bank import apply_filter

st.title("Image Filter Bank")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
   # Read image
   file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
   image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # Ensure the color format

   # Display original image
   st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Original Image', use_column_width=True)


   # Filter selection
   filters_list = ["Grayscale", "Blur", "Edge Detection", "Sepia", "Invert Colors",
                  "Sharpen", "Emboss", "Cartoonize", "Box Blur"]
   filter_options = {filter: st.checkbox(filter) for filter in filters_list}

   if any(value for value in filter_options.values()):
       # Apply selected filters
       for filter, checked in filter_options.items():
           if checked:
               image = apply_filter(image, filter)
       st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Filtered Image', use_column_width=True)

   if st.button("Reset"):
       # Reset image to original
       st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Original Image', use_column_width=True)
