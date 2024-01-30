import cv2
import os

# Define the folder containing the saved plot images
image_folder = 'temp_images'

# Define the video output file
video_name = 'covid_dashboard_video.mp4'

# Get a list of all image files in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Initialize the video writer
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height))

# Write each image to the video
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

# Release the video writer
cv2.destroyAllWindows()
video.release()

# Remove the temporary image files
for image in images:
    os.remove(os.path.join(image_folder, image))