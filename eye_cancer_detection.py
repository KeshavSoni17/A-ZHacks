import cv2
import numpy as np
import time

def filter_eye(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (3,3))
    detected_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 5, maxRadius = 40)
    if detected_circles is not None: 
        detected_circles = np.uint16(np.around(detected_circles)) 
  
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            img  = img[b-r:b+r,a-r:a+r]
            _, img = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
            return img

        
def classify_eye(img):
    img = filter_eye(img)
    count = 0
    try:
        imgWidth = len(img)
        imgHeight = len(img[1])
    except:
        return False
    for x in range(0, imgWidth):
        for y in range(0,imgHeight):
            if (img[x][y])==255:
                count = count + 1
       
    if(int(len(img)*len(img[1])/2)<count):
        return True
    else:
        return False

        
