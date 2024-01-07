import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tkinter import filedialog
from point_reader import point_reader
from utils import draw_lines_and_point

def vanishing_point(img):
    marked_points = point_reader(img)
    
    if len(marked_points) != 4:
        print("Please mark exactly four points on two lines.")
        return
    
    line1 = marked_points[:2]
    line2 = marked_points[2:]

    line1_coeffs = np.polyfit([line1[0][0], line1[1][0]], [line1[0][1], line1[1][1]], 1)
    line2_coeffs = np.polyfit([line2[0][0], line2[1][0]], [line2[0][1], line2[1][1]], 1)

    intersection_x = (line2_coeffs[1] - line1_coeffs[1]) / (line1_coeffs[0] - line2_coeffs[0])
    intersection_y = line1_coeffs[0] * intersection_x + line1_coeffs[1]
    
    return (int(intersection_x), int(intersection_y)), line1, line2



def select_image():
    # Get the current working directory
    current_directory = os.getcwd()
   
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(initialdir=current_directory)
    if file_path:        
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image to RGB for display
        
        # Display the image in Tkinter window
        image = Image.fromarray(img)
        image_tk = ImageTk.PhotoImage(image)
        
        label = tk.Label(root, image=image_tk)
        label.image = image_tk
        label.pack()
        
        # Get vanishing point coordinates
        vanishing_point_coord, line1, line2 = vanishing_point(img)
        

        print("Vanishing Point Coordinates:", vanishing_point_coord)

        # Display lines and vanishing point on the image
        img_with_lines = draw_lines_and_point(img, line1, line2, vanishing_point_coord)

        # Display the updated image in the Tkinter window
        updated_image = Image.fromarray(img_with_lines)
        updated_image_tk = ImageTk.PhotoImage(updated_image)

        label.config(image=updated_image_tk)
        label.image = updated_image_tk

root = tk.Tk()
root.title("Vanishing Point Detection")
root.geometry("600x400")

button = tk.Button(root, text="Select Image", command=select_image)
button.pack()

root.mainloop()