import cv2
import numpy as np

def homo(src_points, dst_points):
    A = []
    for i in range(len(src_points)):
        x, y = src_points[i]
        u, v = dst_points[i]
        A.append([-x, -y, -1, 0, 0, 0, x * u, y * u, u])
        A.append([0, 0, 0, -x, -y, -1, x * v, y * v, v])

    A = np.array(A)
    return A


def stitch_images(img1, img2, dest_points, src_points):

    YOUR_HOMOGRAPHY_MATRIX = homo(dest_points, src_points)

    u, s, vh = np.linalg.svd(YOUR_HOMOGRAPHY_MATRIX)
    vh = np.transpose(vh)
    P = vh[:, len(vh[0]) - 1]

    P = np.array([P[0:3], P[3:6], P[6:9]])

    h1, w1 = img1.shape[:2]

    P = P.astype(np.float64)

    stitched_img = cv2.warpPerspective(img2, P, (w1 + img2.shape[1], h1))
    stitched_img[:h1, :w1] = img1

    return stitched_img
