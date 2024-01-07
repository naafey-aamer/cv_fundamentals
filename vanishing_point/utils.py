import cv2
import numpy as np


def extend_line_to_endpoint(line, image_shape):
    point1, point2 = line
    
    # Calculate slope and intercept
    if point2[0] - point1[0] != 0:  # Ensure non-vertical line (to avoid division by zero)
        slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    else:
        slope = np.inf  # Vertical line
    
    intercept = point1[1] - slope * point1[0]
    
    if slope == 0:
        x1, y1 = int(point1[0]), 0
        x2, y2 = int(point1[0]), image_shape[0]
    elif np.isinf(slope):
        x1, y1 = 0, int(intercept)
        x2, y2 = image_shape[1], int(intercept)
    else:
        x1, y1 = 0, int(intercept)
        x2 = int((image_shape[0] - intercept) / slope)
        y2 = image_shape[0]
        
        if x2 < 0 or x2 >= image_shape[1]:
            x1 = image_shape[1]
            y1 = int(slope * x1 + intercept)
    
    return [(x1, y1), (x2, y2)]


def draw_lines_and_point(img, line1, line2, vanishing_point_coord):
    img_with_lines = img.copy()
    
    # Extend lines to image edges
    extended_line1 = extend_line_to_endpoint(line1, img.shape[:2])
    extended_line2 = extend_line_to_endpoint(line2, img.shape[:2])
    
    cv2.line(img_with_lines, tuple(extended_line1[0]), tuple(extended_line1[1]), (255, 0, 0), 2)
    cv2.line(img_with_lines, tuple(extended_line2[0]), tuple(extended_line2[1]), (255, 0, 0), 2)
    
    cv2.circle(img_with_lines, vanishing_point_coord, 5, (0, 255, 0), -1)
    
    return img_with_lines