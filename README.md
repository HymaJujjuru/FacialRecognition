# 🎭 Real-Time Facial Expression Recognition  

## Overview  
This project uses **OpenCV** and **FER (Facial Expression Recognition)** to detect and label facial expressions **in real-time** using a webcam.  
The program first detects faces using OpenCV’s **Haar Cascade classifier** and then analyzes emotions using FER.  

---

## 🚀 Features  
✅ **Real-time emotion detection** using a webcam  
✅ **Accurate face filtering** with OpenCV  
✅ **Larger, readable labels** with colorblind-friendly colors  
✅ **Easy to use** – just run the script and look at the camera!  

---

## 🛠️ Installation  

### 1️⃣ Install Dependencies  
Ensure you have Python installed, then install the required libraries:  

```bash
pip install opencv-python fer
```

### 2️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/facial-expression-recognition.git
cd facial-expression-recognition
```

### 3️⃣ Run the Program  
```bash
python face_expression_recognition.py
```
> **Press 'q'** to exit the program anytime.

---

## ⚙️ How It Works  
1. **Opens the webcam** and captures video frames.  
2. **Detects faces** using OpenCV’s **Haar Cascade classifier**.  
3. **Analyzes facial expressions** using the `fer` library.  
4. **Displays real-time emotion labels** over detected faces.  

### 🎭 Supported Emotions  
😃 **Happy** | 😠 **Angry** | 😢 **Sad** | 😮 **Surprised** | 😐 **Neutral** | 😨 **Fearful** | 🤢 **Disgusted**  

---

## 🖼️ Example Output  
![Demo GIF](https://your-demo-image-link.gif)  

---

## 🎨 Customization  
You can modify:  
🔹 **Bounding box color** – Change `(255, 165, 0)` for different colors.  
🔹 **Font size & thickness** – Adjust `cv2.FONT_HERSHEY_SIMPLEX, 1.0, 3`.  
🔹 **Face detection sensitivity** – Modify `scaleFactor` and `minNeighbors`.  

---

## ❓ Troubleshooting  
🔹 **Webcam not opening?** Try `cap = cv2.VideoCapture(1)` if you have multiple cameras.  
🔹 **Low accuracy?** Ensure good lighting and a clear background.  
🔹 **Not detecting emotions?** Try increasing the face size by adjusting `minSize=(50, 50)`.  

---

## 📜 Code Explanation  
The script follows these steps:  

1️⃣ **Initialize Webcam**  
- The program starts by opening the webcam and capturing frames.  
- If the webcam fails to open, it prints an error message.  

2️⃣ **Face Detection**  
- Uses OpenCV’s **Haar Cascade classifier** to detect faces in each frame.  
- Converts the frame to **grayscale** for better accuracy.  

3️⃣ **Facial Expression Recognition**  
- Extracts the face region from the frame.  
- Uses the `fer` library to analyze emotions and get confidence scores.  

4️⃣ **Draw Bounding Boxes & Labels**  
- Draws an **orange** bounding box around each detected face.  
- Displays **emotion labels** with a **larger font** and a **black outline** for readability.  

5️⃣ **Exit on 'q'**  
- The program runs in a loop until the user **presses 'q'** to close the window.  

---

## 🤝 Contributing  
Feel free to **fork** this repo, create a new branch, and submit a **pull request**! Contributions are welcome.  

---

## 📜 License  
This project is open-source under the **MIT License**.  