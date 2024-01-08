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
    
    # Calculate intersection points with image borders
    x1, y1 = 0, int(intercept)
    x2, y2 = image_shape[1], int(slope * image_shape[1] + intercept)
    
    if y1 < 0 or y1 >= image_shape[0]:
        y1 = 0
        x1 = int((y1 - intercept) / slope)
    
    if y2 < 0 or y2 >= image_shape[0]:
        y2 = image_shape[0] - 1
        x2 = int((y2 - intercept) / slope)
    
    return [(x1, y1), (x2, y2)]

def draw_lines_and_point(img, line1, line2, vanishing_point_coord):
    img_with_lines = img.copy()
    
    # Extend lines to image edges
    extended_line1 = extend_line_to_endpoint(line1, img.shape[:2])
    extended_line2 = extend_line_to_endpoint(line2, img.shape[:2])
    
    # Draw extended lines
    cv2.line(img_with_lines, tuple(extended_line1[0]), tuple(extended_line1[1]), (255, 0, 0), 2)
    cv2.line(img_with_lines, tuple(extended_line2[0]), tuple(extended_line2[1]), (255, 0, 0), 2)
    
    # Draw circles at endpoints of line1 and line2
    cv2.circle(img_with_lines, tuple(line1[0]), 5, (0, 0, 255), -1)  # Red circle for line1 point1
    cv2.circle(img_with_lines, tuple(line1[1]), 5, (0, 0, 255), -1)  # Red circle for line1 point2
    cv2.circle(img_with_lines, tuple(line2[0]), 5, (0, 0, 255), -1)  # Red circle for line2 point1
    cv2.circle(img_with_lines, tuple(line2[1]), 5, (0, 0, 255), -1)  # Red circle for line2 point2
    
    # Draw vanishing point
    cv2.circle(img_with_lines, vanishing_point_coord, 5, (0, 255, 0), -1)
    
    return img_with_lines