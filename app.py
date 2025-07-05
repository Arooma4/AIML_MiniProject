from flask import Flask, request, jsonify
import os
import cv2
import mediapipe as mp
import json
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load ML model once
df = pd.read_csv('measurements.csv')
X = df[['chest_cm', 'waist_cm', 'hip_cm']]
y = df['size']
clf = DecisionTreeClassifier().fit(X, y)

def pixel_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def estimate_measurements(image_path, user_height_cm):
    image = cv2.imread(image_path)
    image_height, image_width, _ = image.shape
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose(static_image_mode=True)

    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    landmark_names = {
        11: 'left_shoulder',
        12: 'right_shoulder',
        23: 'left_hip',
        24: 'right_hip',
        0: 'nose',
        27: 'left_ankle',
        28: 'right_ankle'
    }

    keypoints = {}
    if results.pose_landmarks:
        for idx, lm in enumerate(results.pose_landmarks.landmark):
            if idx in landmark_names:
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)
                keypoints[landmark_names[idx]] = (x, y)

        head_y = keypoints['nose'][1]
        ankle_y = int((keypoints['left_ankle'][1] + keypoints['right_ankle'][1]) / 2)
        pixel_height = ankle_y - head_y
        cm_per_pixel = user_height_cm / pixel_height

        shoulder_px = pixel_distance(keypoints['left_shoulder'], keypoints['right_shoulder'])
        shoulder_cm = shoulder_px * cm_per_pixel

        hip_px = pixel_distance(keypoints['left_hip'], keypoints['right_hip'])
        hip_cm = hip_px * cm_per_pixel

        # Approximate chest and waist using heuristics (adjust as needed)
        chest_cm = shoulder_cm * 0.9
        waist_cm = hip_cm * 0.9

        return {
            "height_cm": user_height_cm,
            "shoulder_cm": round(shoulder_cm, 2),
            "hip_cm": round(hip_cm, 2),
            "chest_cm": round(chest_cm, 2),
            "waist_cm": round(waist_cm, 2)
        }

    else:
        return None

@app.route('/predict', methods=['POST'])
def predict_size():
    user_height = float(request.form['height'])
    image_file = request.files['front']
    front_path = os.path.join(UPLOAD_FOLDER, 'front.jpg')
    image_file.save(front_path)

    measurements = estimate_measurements(front_path, user_height)

    if not measurements:
        return jsonify({"error": "Pose landmarks not detected. Please check the image."}), 400

    user_input = pd.DataFrame([[measurements['chest_cm'], measurements['waist_cm'], measurements['hip_cm']]],
                              columns=['chest_cm', 'waist_cm', 'hip_cm'])
    predicted_size = clf.predict(user_input)[0]

    return jsonify({
        "measurements": measurements,
        "predicted_size": predicted_size
    })

if __name__ == "__main__":
    app.run(debug=True)
