import cv2
import numpy as np
import streamlit as st
from homography import homo, stitch_images
from point_reader import point_reader

def main():
  st.title('Image Stitching App')

  st.markdown("""
  1. Once you have uploaded the images, 2 popups will open.
  2. Kindly select corresponding points alternatively. That is, select a point in the 1st image, choose its correspondence in the 2nd image, then choose another point in image1 and so on...
  """)

  col1, col2 = st.columns(2)
  uploaded_file1 = col1.file_uploader("Upload Image 1", type=['png', 'jpg'])
  uploaded_file2 = col2.file_uploader("Upload Image 2", type=['png', 'jpg'])

  if uploaded_file1 is not None and uploaded_file2 is not None:
      img1 = cv2.imdecode(np.fromstring(uploaded_file1.read(), np.uint8), 1)
      img2 = cv2.imdecode(np.fromstring(uploaded_file2.read(), np.uint8), 1)

      col1, col2 = st.columns(2)

      img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
      img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) 
      col1.image(img1, caption='Image 1', use_column_width=True)
      col2.image(img2, caption='Image 2', use_column_width=True)

      src_points, dest_points = point_reader(img1, img2)

      # Combine the first image (hss1) with the warped second image (hss2)
      stitched_img = stitch_images(img1, img2, dest_points, src_points)

    #   stitched_img = cv2.cvtColor(stitched_img, cv2.COLOR_BGR2RGB)      
      st.image(stitched_img, caption='Stitched Image', use_column_width=True)

if __name__ == "__main__":
  main()