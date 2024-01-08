# cv_fundamentals
This repository aims to be an educative resource covering interactive implementations of the founding concepts of Computer Vision taught in **CS5613: Computer Vision Fundamentals** at LUMS, Pakistan.

## Installation
Clone the repository and install the required packages with:
```
pip3 install -r requirements.txt
```
## Vanishing Point
<details>
<summary>Click to expand</summary>
<br>
  Vanishing points refer to the points in a perspective image where parallel lines appear to converge or intersect. They are the foundation of projective geometry and play a major role in understanding the spatial relationships between objects in a scene, aiding in tasks like object detection, 3D reconstruction, and image rectification. In Stanley Kubrick's films like "The Shining" and "2001: A Space Odyssey," his use of one-point perspective illustrates this concept vividly.
<br>
<br>

The code provided in the folder `vanishing point` utilizes Tkinter for the GUI, and OpenCV for image handling. Here's a brief overview of how to interact with it:

1. **Run "_main.py"** to open a window with an "upload file" button. Upload an image to display it.:
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/vanishing_point/images/shing.png)

2. **Mark 4 Points:** Another window will open after image upload. Mark points for two converging parallel lines in order.
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/vanishing_point/images/shining_points_marked.png)

3. **Vanishing Point:** The updated image will show the vanishing point marked in green.
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/vanishing_point/images/result.png)

4. **TO-DO:** Implement vanishing points calculation for 2-point and 3-point perspective.
</details>

## Image Stitching
<details>
<summary>Click to expand</summary>
<br>

  In image stitching, homography serves as the cornerstone. It's a transformation matrix that maps points from one image to another, enabling alignment and blending. By identifying corresponding points in multiple images, the homography matrix helps warp and merge these images seamlessly. This process aligns the images according to the perspective from which they were taken, ultimately creating a panoramic or stitched image. **Atleast 4 points** are required to find the transformation matrix.

![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/stitch_images/images/OkwaB.png)

**Note:** The following implementation is purely based on the equations above :arrow_up:. Correspondence error correction techniques like RANSAC have not been incorporated so kindly mark your correspondences with precision.

The code in the folder `stitch_images` is an Image Stitching App built using Streamlit and OpenCV. It enables users to upload two images and select corresponding points on these images. The app applies homography to stitch the images together based on the chosen points to create a panorama-like image.

1. **Run Streamlit App** using the command `streamlit run _main.py`
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/stitch_images/images/streamlit_initial.png)

2. **Image Upload** Upload two images.
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/stitch_images/images/uploaded_images.png)

4. **Point Selection:** Mark atleast 4 corresponding points on both images alternatively.
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/stitch_images/images/correspondences.png)

5. **Stitching:** The app calculates a homography matrix based on the selected points and stitches the images together to create a panoramic view.
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/stitch_images/images/stitched_result_naala.jpg)
</details>

## Structure From Motion (SFM)
<details>
<summary>Click to expand</summary>
</details>
