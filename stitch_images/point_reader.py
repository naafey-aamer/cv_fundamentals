import cv2

def point_reader(img1, img2):
 # Create separate windows for each image
 cv2.namedWindow('Image 1 - Select points', cv2.WINDOW_NORMAL)
 cv2.namedWindow('Image 2 - Select corresponding points', cv2.WINDOW_NORMAL)
 cv2.resizeWindow('Image 1 - Select points', img1.shape[1], img1.shape[0])
 cv2.resizeWindow('Image 2 - Select corresponding points', img2.shape[1], img2.shape[0])

 # Display the images
 cv2.imshow('Image 1 - Select points', img1)
 cv2.imshow('Image 2 - Select corresponding points', img2)

 # Initialize lists to store marked points for both images
 src_points, dest_points = [], []

 # Flag to keep track of which image to select points from
 select_from_img1 = True

 def get_points(event, x, y, flags, param):
     nonlocal select_from_img1
     if event == cv2.EVENT_LBUTTONDOWN:
         if select_from_img1:
             points_list = src_points
             cv2.circle(img1, (x, y), 20, (0, 0, 255), -1)
             cv2.imshow('Image 1 - Select points', img1)
             select_from_img1 = False
         else:
             points_list = dest_points
             cv2.circle(img2, (x, y), 20, (0, 255, 0), -1)
             cv2.imshow('Image 2 - Select corresponding points', img2)
             select_from_img1 = True

         points_list.append((x, y))

 cv2.setMouseCallback('Image 1 - Select points', get_points)
 cv2.setMouseCallback('Image 2 - Select corresponding points', get_points)

 while True:
     key = cv2.waitKey(1)
     if key == 27: # Press ESC to exit and return the selected points
         cv2.destroyAllWindows()
         return src_points, dest_points