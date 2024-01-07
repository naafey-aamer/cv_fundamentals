import cv2
import numpy as np
import matplotlib.pyplot as plt

def point_reader(img):
    # Display the image using matplotlib
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Mark points for vanishing point calculation. Close the window when done.')
    plt.axis('on')
    plt.gca().set_axis_off()

    # List to store the marked points
    points = []

    def onclick(event):
        # Extract x, y coordinates of the click
        x = int(round(event.xdata))
        y = int(round(event.ydata))
        points.append((x, y))
        # Plot a point where the user clicked
        plt.scatter(x, y, color='red')
        plt.draw()

    # Connect the click event to the function
    cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    # Ensure exactly four points are marked for vanishing point calculation
    if len(points) != 4:
        print("Please mark exactly four points for vanishing point calculation.")
        return []

    # Convert points to a numpy array
    points_array = np.array(points)

    return points_array
