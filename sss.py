import cv2
import numpy as np
import serial
import time
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('drowsiness_detection_model better.h5')

# Load Haar Cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize Serial Communication with Arduino
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)  # ⚠️ Change COM port if needed
time.sleep(2)  # Wait for Arduino to initialize

# Start video capture
cap = cv2.VideoCapture(0)

# Label mapping
label_map = {0: 'Drowsy', 1: 'Awake'}

# Function to send signal to Arduino
def send_signal(value):
    arduino.write(f"{value}\n".encode())

def detect_drowsiness():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        status = "Awake"  # Default status

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            if len(eyes) >= 2:
                status = "Awake"
                color = (0, 255, 0)  # Green
            else:
                status = "Drowsy"
                color = (0, 0, 255)  # Red

            # Draw box and label
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Send signal to Arduino
        if status == "Drowsy":
            send_signal(1)
        else:
            send_signal(0)

        # Display the frame
        cv2.imshow('Drowsiness Detection', frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Start detection
detect_drowsiness()

# Clean up
cap.release()
cv2.destroyAllWindows()
arduino.close()
