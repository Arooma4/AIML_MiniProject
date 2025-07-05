import cv2
import mediapipe as mp

# User-defined height in cm (ask this in your form or UI)
USER_HEIGHT_CM = 170  # Example height

# Load front view image
image_path = 'C:\\Users\\aditri sharma\\OneDrive - Noida Institute of Engineering and Technology\\Desktop\\mini project 6 sem\\FASHION\\img_front.png'
image = cv2.imread(image_path)

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(static_image_mode=True)

# Convert to RGB and process
results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# Get image dimensions
image_height, image_width, _ = image.shape

# List of important landmark indexes
landmark_names = {
    11: 'left_shoulder',
    12: 'right_shoulder',
    23: 'left_hip',
    24: 'right_hip',
    0: 'nose',
    27: 'left_ankle',
    28: 'right_ankle'
}

# Store extracted keypoints
keypoints = {}

if results.pose_landmarks:
    for idx, lm in enumerate(results.pose_landmarks.landmark):
        if idx in landmark_names:
            x = int(lm.x * image_width)
            y = int(lm.y * image_height)
            keypoints[landmark_names[idx]] = (x, y)
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

    # Draw landmarks for visual check
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Save or show the image
    cv2.imwrite("pose_output.jpg", image)

    # Calculate pixel-based measurements
    def pixel_distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

    # Get total body height in pixels (from nose to average ankle position)
    head_y = keypoints['nose'][1]
    ankle_y = int((keypoints['left_ankle'][1] + keypoints['right_ankle'][1]) / 2)
    pixel_height = ankle_y - head_y
    cm_per_pixel = USER_HEIGHT_CM / pixel_height

    # Shoulder width in pixels and cm
    shoulder_px = pixel_distance(keypoints['left_shoulder'], keypoints['right_shoulder'])
    shoulder_cm = shoulder_px * cm_per_pixel

    # Hip width in pixels and cm
    hip_px = pixel_distance(keypoints['left_hip'], keypoints['right_hip'])
    hip_cm = hip_px * cm_per_pixel

    print("\n📏 Body Measurement Results")
    print(f"User Height: {USER_HEIGHT_CM} cm")
    print(f"Total Pixel Height: {pixel_height:.2f} px")
    print(f"Shoulder Width: {shoulder_cm:.2f} cm")
    print(f"Hip Width: {hip_cm:.2f} cm")

else:
    print("⚠️ No pose landmarks detected. Check image quality.")

import json

# Save to JSON for MakeHuman
measurement_data = {
    "height": round(USER_HEIGHT_CM / 100, 2),  # convert to meters
    "shoulderWidth": round(shoulder_cm / 100, 2),
    "hipWidth": round(hip_cm / 100, 2)
}

with open("output_measurements.json", "w") as f:
    json.dump(measurement_data, f, indent=4)

print("\n✅ Measurements saved to output_measurements.json")


# Cleanup
pose.close()

