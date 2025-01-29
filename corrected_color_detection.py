import cv2
import numpy as np

# Initialize camera capture
cam = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

cv2.namedWindow('Colour Detection')

def window(x):
    pass

# Create trackbars for Hue, Saturation, and Value
cv2.createTrackbar('Hue', 'Colour Detection', 0, 179, window)
cv2.createTrackbar('Saturation', 'Colour Detection', 0, 255, window)
cv2.createTrackbar('Value', 'Colour Detection', 0, 255, window)

# Wait for a short time to ensure the window and trackbars are created
cv2.waitKey(1000)

while(True):
    # Capture frame from webcam
    ret, img = cam.read()
    
    if not ret:
        print("Error: Failed to grab frame.")
        break
    
    img = np.flip(img, axis=1)  # Flip the image horizontally
    img = cv2.resize(img, (480, 360))  # Resize the image
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV
    blurred = cv2.GaussianBlur(hsv, (11, 11), 0)  # Apply Gaussian Blur

    # Get the trackbar positions for Hue, Saturation, and Value
    h = cv2.getTrackbarPos('Hue', 'Colour Detection')
    s = cv2.getTrackbarPos('Saturation', 'Colour Detection')
    v = cv2.getTrackbarPos('Value', 'Colour Detection')

    # Print trackbar values for debugging purposes
    print(f"Hue: {h}, Saturation: {s}, Value: {v}")

    lower_colour = np.array([h, s, v])  # Lower HSV bound
    upper_colour = np.array([180, 255, 255])  # Upper HSV bound

    # Create a mask based on the selected HSV range
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    result = cv2.bitwise_and(img, img, mask=mask)

    # Show the result in the 'Colour Detection' window
    cv2.imshow('Colour Detection', result)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break  # Exit if 'q' is pressed

# Release the webcam and close windows
cam.release()
cv2.destroyAllWindows()

# After exiting the loop, prompt the user to enter the final values
try:
    print("Please enter the final HSV values that you have detected using the menu.")
    final_h = int(input("Enter final Hue (0-179): "))
    final_s = int(input("Enter final Saturation (0-255): "))
    final_v = int(input("Enter final Value (0-255): "))

    print(f"Final values set to: Hue={final_h}, Saturation={final_s}, Value={final_v}")

except ValueError:
    print("Invalid input. Please enter numeric values within the valid range.")
