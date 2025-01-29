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
