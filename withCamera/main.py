import cv2  # OpenCV for image processing and webcam capture
from fer import FER  # Facial Expression Recognition (FER) library

# Load OpenCV's pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def real_time_expression_recognition():
    """
    Captures real-time video from the webcam, detects faces, and labels their facial expressions.
    Uses OpenCV for face detection and the FER library for emotion recognition.
    """

    # Initialize the FER detector
    detector = FER()

    # Open the webcam (0 = default camera)
    cap = cv2.VideoCapture(0)

    # Check if the webcam opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame-by-frame from webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Convert frame to grayscale (improves face detection accuracy)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces using OpenCV's Haar Cascade classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

        # Process each detected face
        for (x, y, w, h) in faces:
            # Crop the face region from the frame
            face_region = frame[y:y+h, x:x+w]  

            # Use FER to detect emotions in the cropped face
            result = detector.detect_emotions(face_region)

            if result:
                emotions = result[0]['emotions']  # Extract emotion scores from the result

                # Draw a bounding box around the detected face (now in **orange**)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 165, 0), 3)

                # Display detected emotions as text labels
                y_offset = 30  # Increased spacing for better readability
                for emotion, score in emotions.items():
                    text = f"{emotion}: {score:.2f}"  # Format label with confidence score
                    
                    # Bigger font size and colorblind-friendly **white text with black outline**
                    cv2.putText(frame, text, (x, y - y_offset), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 3, cv2.LINE_AA)  # White text, thicker
                    cv2.putText(frame, text, (x, y - y_offset), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 1, cv2.LINE_AA)  # Black outline
                    y_offset += 35  # Move next label slightly lower

        # Show the frame with bounding boxes and emotion labels
        cv2.imshow("Real-Time Facial Expression Recognition", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows when the loop ends
    cap.release()
    cv2.destroyAllWindows()

# Run the real-time facial expression recognition
real_time_expression_recognition()
