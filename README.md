# VIRTUAL DRIVE

## Project Overview
**VIRTUAL DRIVE** is a real-time webcam-based color detection system designed to provide hands-free controls for racing games such as **Asphalt 9: Legends**. By detecting hand movements and specific color markers, the program translates real-world motions into in-game actions like steering and activating nitro boosts.

## Features
- **Real-time color detection** using OpenCV.
- **Virtual steering** through hand movements.
- **Game control automation** via key presses using `ctypes`.
- **Optimized for Asphalt 9: Legends** and similar racing games.
- **Simple and intuitive interface** with HSV trackbars for fine-tuning color detection.

## Files in the Project

### 1. `corrected_color_detection.py`
This script captures real-time video feed, detects colors using HSV filtering, and allows the user to fine-tune the detection settings.

### 2. `directkeys.py`
Handles sending keyboard inputs to simulate key presses required for in-game actions.

### 3. `drum.py`
The main script that integrates color detection with game controls. It:
- Uses OpenCV to process the webcam feed.
- Identifies movement for left, right, and nitro boost.
- Simulates key presses (`A`, `D`, and `Space`) based on detected movements.

## Installation & Requirements

### Prerequisites
Ensure you have Python installed, along with the following dependencies:

```sh
pip install numpy opencv-python imutils
```

# Running the Project

## Requirements
- A connected webcam
- Python installed on your system

## How to Run
1. Connect a webcam to your system.
2. Run the script:
   ```sh
   python drum.py
3. Adjust the HSV values using `corrected_color_detection.py` if needed.
4. Open *Asphalt 9* or a similar game and start playing using hand gestures!

## Controls
- **Move your hand left** → Steers left (`A` key press)
- **Move your hand right** → Steers right (`D` key press)
- **Move your hand down** → Activates nitro (`Space` key press)
- **Press 'q'** → Exit the program

## Notes
- Ensure good lighting conditions for better color detection.
- Adjust the HSV values in `corrected_color_detection.py` for optimal performance.
- Designed for **Windows OS** due to keyboard simulation using `ctypes`.

## Author
This project was developed as part of a **Semester 5 Mini Project** by **[Viraj Bele,Siddhi Lipare,Saniya Chavan,Hardik Tandale]**. Guided by **Dr. P S More Ma'am**.

## Acknowledgments
Special thanks to:
- **OpenCV and NumPy** community


