import cv2
import numpy as np

# Function to apply different filters
def apply_filter(image, filter_name):
    if filter_name == "Grayscale":
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    elif filter_name == "Blur":
        return cv2.GaussianBlur(image, (11, 11), 0)

    elif filter_name == "Edge Detection":
        return cv2.Canny(image, 100, 200)

    elif filter_name == "Sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        return cv2.filter2D(image, -1, kernel)

    elif filter_name == "Invert Colors":
        return cv2.bitwise_not(image)

    elif filter_name == "Sharpen":
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        return cv2.filter2D(image, -1, kernel)

    elif filter_name == "Emboss":
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])
        return cv2.filter2D(image, -1, kernel)

    elif filter_name == "Cartoonize":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 7)
        edges = cv2.Laplacian(blur, cv2.CV_8U, ksize=5)
        edges = 255 - edges
        _, thresh = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY_INV)
        return cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

    elif filter_name == "Box Blur":
        ksize = 15 # Kernel size
        return cv2.boxFilter(image, -1, (ksize, ksize))

    elif filter_name == "60TVs":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        noise = np.random.randint(-20, 20, gray.shape)
        gray = gray + noise
        gray[gray < 0] = 0
        gray[gray > 255] = 255
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

