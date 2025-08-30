🚗 Drowsy Driver Detection using ML, OpenCV, and IoT
📌 Overview

This project detects driver drowsiness in real-time using Machine Learning, OpenCV, and IoT integration with Arduino.
A camera monitors the driver’s eyes, and if drowsiness is detected, the system triggers a buzzer and LED connected to Arduino to alert the driver.

🗂️ Project Files

drowsiness_detection_model.h5 → Pre-trained deep learning model for drowsiness detection.

Drowsy Working.ipynb → Jupyter Notebook for training, testing, and experimenting with the ML model.

sss.py → Main Python script for real-time detection and Arduino signal transmission.

Wiring Diagram.png → Circuit diagram for Arduino UNO with buzzer and LED.

⚡ Hardware Requirements

Arduino UNO

USB Cable

Buzzer

LED + 220Ω Resistor

Camera (Webcam or USB)

Jumper Wires

Breadboard

🖥️ Software Requirements

Python 3.8+

OpenCV

NumPy

TensorFlow / Keras

pySerial (for Arduino communication)

Jupyter Notebook (for .ipynb file)

Arduino IDE

🔌 Circuit Connection

LED → Digital Pin 8 (with 220Ω resistor)

Buzzer → Digital Pin 6

VCC & GND → 5V and GND of Arduino

Communication → Python sends signals (0 = Awake, 1 = Drowsy) via Serial to Arduino

▶️ How to Run

Upload Arduino sketch to handle buzzer + LED (ensure baud rate = 9600).

Connect Arduino UNO via USB.

Run Python script:
python sss.py

<img width="1536" height="1024" alt="Arduino Uno with Drowsiness Detection System" src="https://github.com/user-attachments/assets/76980e48-a5c9-43ef-80ed-2286acc8f7c5" />

📊 Workflow

Camera Input → Captures driver’s face.

OpenCV + ML Model → Detects eyes & predicts drowsiness.

Python → Arduino → Sends alert signals via serial.

Arduino → Activates buzzer and LED to wake driver.

🚀 Future Enhancements

Send drowsiness alerts to mobile via IoT (ESP32, GSM module).

Log driver behavior for fleet monitoring.

Improve detection accuracy with deep learning models.
