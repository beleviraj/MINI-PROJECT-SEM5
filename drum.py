import numpy as np
import cv2
import imutils
from imutils.video import VideoStream
from directkeys import PressKey, A, D, Space, ReleaseKey

# Initialize the video stream
cam = VideoStream(src=0).start()
currentKey = list()

while True:    
    key = False   

    img = cam.read()
    img = np.flip(img, axis=1)              
    img = imutils.resize(img, width=640)                                                                                                                            
    img = imutils.resize(img, height=480)                                             

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (11, 11)
    blurred = cv2.GaussianBlur(hsv, value, 0)                                                                                                                                                                                                                                                             
    colourLower = np.array([70,123, 95])
    colourUpper = np.array([180, 255, 255])                                                                                                            

    height = img.shape[0]
    width = img.shape[1]

    mask = cv2.inRange(blurred, colourLower, colourUpper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    upContour = mask[0:height//2, 0:width]
    downContour = mask[3*height//4:height, 2*width//5:3*width//5]

    cnts_up = cv2.findContours(upContour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts_up = imutils.grab_contours(cnts_up)

    cnts_down = cv2.findContours(downContour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts_down = imutils.grab_contours(cnts_down)

    if len(cnts_up) > 0:
        c = max(cnts_up, key=cv2.contourArea)
        M = cv2.moments(c)
        cX = int(M["m10"] / (M["m00"] + 0.000001))

        if cX < (width // 2 - 55):
            PressKey(A)
            key = True
            currentKey.append(A)
        elif cX > (width // 2 + 55):
            PressKey(D)
            key = True
            currentKey.append(D)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    
    if len(cnts_down) > 0:
        PressKey(Space)
        key = True
        currentKey.append(Space)
    
    # Draw rectangles and update text/boundary colors
    rect_size = height // 2  # Use height to define the size to keep it a square

    img = cv2.rectangle(img, (width//2 - rect_size - 40, 0), (width//2 - 40, rect_size), (0, 0, 255), 2)
    cv2.putText(img, 'LEFT', (width//2 - rect_size + 10, rect_size // 2), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)

    img = cv2.rectangle(img, (width//2 + 40, 0), (width//2 + rect_size + 40, rect_size), (0, 0, 255), 2)
    cv2.putText(img, 'RIGHT', (width//2 + 50, rect_size // 2), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)

    img = cv2.rectangle(img, (2*width//5, 3*height//4), (3*width//5, height), (0, 0, 255), 2)
    cv2.putText(img, 'NITRO', (2*width//5 + 10, 3*height//4 + (height - 3*height//4)//2), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Steering", img)

    if not key and len(currentKey) != 0:
        for current in currentKey:
            ReleaseKey(current)
        currentKey = list()

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
