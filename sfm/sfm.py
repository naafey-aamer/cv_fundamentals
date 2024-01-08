import numpy as np
import cv2

# def find_correct_camera_poses(points1, points2, K):
#     # Calculate Fundamental Matrix
#     F, _ = cv2.findFundamentalMat(points1, points2, cv2.FM_RANSAC)

#     # Calculate Essential Matrix
#     E = np.dot(K.T, np.dot(F, K))

#     # Decompose Essential Matrix to obtain four possible camera poses
#     poses, _, _, _ = cv2.decomposeEssentialMat(E)
    
#     # Triangulate 3D points for each possible pose and find the correct one
#     for i in range(4):
#         R = poses[:, :, i]
#         t = np.array([[poses[0, 3, i]], [poses[1, 3, i]], [poses[2, 3, i]]])

#         # Create camera matrix for the current pose
#         P = np.hstack((R, t))

#         # Triangulate 3D points
#         points4D_homogeneous = cv2.triangulatePoints(np.eye(3), P, points1.T, points2.T)
#         points3D = (points4D_homogeneous / points4D_homogeneous[3]).T[:, :3]

#         # Check depth of triangulated points (in front of the camera)
#         num_points_in_front = np.sum(points3D[:, 2] > 0)

#         if num_points_in_front > len(points3D) * 0.5:  # Assuming at least half points are in front
#             return points3D, R, t

#     # If no valid pose is found, return None
#     return None, None, None


# Function for SfM reconstruction (replace this with your SfM implementation)
def perform_sfm(image_paths):
    # Your SfM reconstruction code here
    # Obtain 3D points and camera poses
    points3D = np.random.rand(100, 3)  # Placeholder for 3D points
    camera_poses = [np.eye(4) for _ in range(10)]  # Placeholder for camera poses
    return points3D, camera_poses

# Function to create a video by panning across the reconstructed scene
def create_panning_video(points3D, camera_poses):
    # Define video parameters
    width, height = 1280, 720  # Define video resolution
    fps = 30  # Frames per second
    video_duration = 10  # Video duration in seconds

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter('panning_video.mp4', fourcc, fps, (width, height))

    # Simulate camera motion and create video frames
    num_frames = fps * video_duration
    for i in range(num_frames):
        # Calculate current camera position (linear interpolation between camera poses)
        current_pose_idx = int(i / num_frames * len(camera_poses))
        current_pose = camera_poses[current_pose_idx]
        current_rotation, current_translation = current_pose[:3, :3], current_pose[:, 3]
        
        # Render frame using the 3D points and camera projection
        frame = np.zeros((height, width, 3), dtype=np.uint8)  # Initialize frame
        
        for point in points3D:
            # Project 3D point to 2D (assuming perspective projection)
            point_2D = np.dot(current_rotation, point) + current_translation
            x, y = int(point_2D[0]), int(point_2D[1])  # Convert to image coordinates
            
            # Check if point is within the frame boundaries
            if 0 <= x < width and 0 <= y < height:
                # Draw points on the frame (adjust for visualization)
                cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)  # Example: draw white points
        
        # Write frame to video
        video_writer.write(frame)

    # Release video writer
    video_writer.release()

# Example usage
# Assuming you have image paths, perform SfM reconstruction
image_paths = ["image1.jpg", "image2.jpg"]  # Replace with actual image paths
points3D, camera_poses = perform_sfm(image_paths)

# Create video by panning across the reconstructed scene
create_panning_video(points3D, camera_poses)
