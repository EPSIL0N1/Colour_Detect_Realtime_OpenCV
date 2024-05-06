import numpy as np
import cv2
from PIL import Image


yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 1, 100, 100
    upperLimit = hsvC[0][0][0] + 1, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit


while True:
    ret, frame = cap.read()
    
    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = get_limits(color=yellow)

    
    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)
    
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
