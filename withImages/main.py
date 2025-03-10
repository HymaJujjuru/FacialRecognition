import cv2
import os
from fer import FER

def label_expressions_in_folder(folder_path):
    # Initialize the facial expression recognizer
    detector = FER()

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Process only image files
            image_path = os.path.join(folder_path, filename)
            print(f"Processing: {image_path}")

            # Load the image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error: Could not load {filename}")
                continue
            
            # Detect facial expressions
            result = detector.detect_emotions(image)
            
            # Display results
            if result:
                for face in result:
                    box = face['box']
                    emotions = face['emotions']

                    # Draw bounding box
                    cv2.rectangle(image, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 2)

                    # Label all detected expressions
                    y_offset = 20
                    for emotion, score in emotions.items():
                        text = f"{emotion}: {score:.2f}"
                        cv2.putText(image, text, (box[0], box[1] - y_offset), 
                                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0, 255, 0), 1, cv2.LINE_AA)
                        y_offset += 20

            else:
                print(f"No face detected in {filename}")
            
            # Show image with results
            cv2.imshow(f'Processed: {filename}', image)
            cv2.waitKey(10000)  # Display each image for 10 seconds
            cv2.destroyAllWindows()

# Example usage
folder_path = 'photos'  # Replace with your actual folder path
label_expressions_in_folder(folder_path)