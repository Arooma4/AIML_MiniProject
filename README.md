**FitAI - AI Powered Body Measuring Solution**

A 3D AI-based body measurement system that automates extraction of human body measurements using a standard camera, visualizing results with realistic 3D models.

**Table of Contents**

- **Overview**
- **Motivation**
- **Features**
- **Tech Stack**
- **Architecture**
- **Installation**
- **Usage**
- **Project Structure**
- **Contributing**
- **License**
- **References**

**Overview**  
FitAI leverages computer vision and AI to detect body keypoints from images and translate them into real-world measurements, then generates a 3D human model using MakeHuman. It targets applications in fashion, fitness, healthcare, and virtual try‑ons.

**Motivation**  
- **E‑commerce Fit Issues:** Reduces high return rates due to size mismatches.  
- **Accessibility:** Enables accurate self‑measurement for users without assistance.  
- **Scalability:** Uses only standard cameras (smartphone or webcam) without specialized hardware.

**Features**  
- **Image Acquisition:** Upload images or use live webcam feed (front and side views).  
- **Keypoint Detection:** Pose estimation via MediaPipe/OpenCV to extract ~33 body landmarks.  
- **Measurement Extraction:** Calculates shoulder width, chest/waist circumference, hip width, arm length, etc.  
- **3D Model Generation:** Creates and exports a MakeHuman (.mhm) model and renders snapshots.  
- **Export Options:** Download measurements in CSV/JSON and 3D models in OBJ/MHM formats.

**Tech Stack**  
- **Backend:** Python, Flask  
- **Computer Vision:** MediaPipe or OpenCV DNN  
- **3D Modeling:** MakeHuman  
- **Frontend:** HTML, CSS, JavaScript (AJAX)  
- **Data Handling:** NumPy, Pandas  
- **Visualization:** Matplotlib  

**Architecture**  
1. **Frontend:** Responsive web interface for image upload and feedback.  
2. **Image Validation:** Format and clarity checks in Flask.  
3. **Pose Detection:** MediaPipe/OpenCV extracts body landmarks.  
4. **Measurement Calculation:** Pixel‑to‑real‑world scaling using reference dimensions.  
5. **3D Generation:** Converts measurements to MakeHuman format and renders model.  
6. **Output:** Displays measurements and 3D snapshots; provides download links.

**Installation**  
1. **Clone the repository:**  
   `git clone https://github.com/Arooma4/FitAI.git`  
   `cd FitAI`  
2. **Create a virtual environment and activate it:**  
   `python3 -m venv venv`  
   `source venv/bin/activate`  (On Windows: `venv\Scripts\activate`)  
3. **Install dependencies:**  
   `pip install -r requirements.txt`  
4. **Install MakeHuman separately** from http://www.makehumancommunity.org  
5. **Run the application:**  
   `flask run`

**Usage**  
1. Navigate to `http://localhost:5000` in your browser.  
2. Upload a clear front‑facing image (or use webcam).  
3. Wait for pose detection and model rendering.  
4. View extracted measurements and download 3D model snapshots.

**Project Structure**  
Project Structure
─────────────────

FitAI/
├── backend/
│   ├── app.py               # Flask application
│   ├── models/              # Pose estimation and utilities
│   └── utils/               # Measurement and scaling logic
├── frontend/
│   ├── index.html
│   └── static/
│       ├── css/
│       └── js/
├── makehuman/
│   └── templates/           # .mhm file generation scripts
├── requirements.txt
└── README.md


**Contributing**  
Contributions are welcome! Please:  
1. **Fork** the repository.  
2. **Create a new branch:** `git checkout -b feature/YourFeature`.  
3. **Commit your changes and push:** `git push origin feature/YourFeature`.  
4. **Open a Pull Request** for review.

**License**  
This project is licensed under the **MIT License**. See LICENSE for details.

**References**  
- Google MediaPipe (2020)  
- MakeHuman Community (2023)  
- OpenCV Library (2023)  
