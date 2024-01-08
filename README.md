# cv_fundamentals
Incremental implementation of the fundamentals of Computer Vision

## Overview
This repository aims to be an educative resource covering interactive implementations of the founding concepts of Computer Vision taught in **CS5613: Computer Vision Fundamentals** at LUMS, Pakistan.

## Installation
Clone the repository and install the required packages with:
```
pip3 install -r requirements.txt
```

## Vanishing Point
Vanishing points refer to the points in a perspective image where parallel lines appear to converge or intersect. They are the foundation of projective geometry and play a major role in understanding the spatial relationships between objects in a scene, aiding in tasks like object detection, 3D reconstruction, and image rectification. In Stanley Kubrick's films like "The Shining" and "2001: A Space Odyssey," his use of one-point perspective illustrates this concept vividly.

The code provided in the folder "vanishing point" utilizes Tkinter for the GUI, and OpenCV for image handling. Here's a brief overview of how to interact with it:

1. **Run "_main.py"** to open a window with an "upload file" button. Upload an image to display it.:
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/vanishing_point/images/shing.png)

2. **Mark 4 Points:** Another window will open after image upload. Mark points for two converging parallel lines in order.
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/vanishing_point/images/shining_points_marked.png)

3. **Vanishing Point:** The updated image will show the vanishing point marked in green.
![image](https://github.com/naafey-aamer/cv_fundamentals/blob/main/vanishing_point/images/result.png)

4. **TO-DO:** Implement vanishing points calculation for 2-point and 3-point perspective.
