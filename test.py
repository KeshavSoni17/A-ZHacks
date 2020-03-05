import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('/Users/sonifamily/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('/Users/sonifamily/Downloads/opencv-master/data/haarcascades/haarcascade_eye.xml')
print(face_cascade)
cap = cv2.VideoCapture(0)


#ret, img = cap.read()
img = cv2.imread("/Users/sonifamily/Desktop/face_image.png")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
        
    eyes = eye_cascade.detectMultiScale(roi_gray)
    print(eyes[0])
    (ex1,ey1,ew1,eh1) = eyes[0]
    cv2.rectangle(roi_color,(ex1,ey1),(ex1+ew1,ey1+eh1),(0,0,0),2)
    print (ex1,ey1,ew1,eh1)
    crop_img1 = roi_color[ey1:ey1+eh1,ex1:ex1+ew1]
    cv2.imwrite("/Users/sonifamily/Desktop/image.jpg",crop_img1)
    (ex2,ey2,ew2,eh2) = eyes[1]
    cv2.rectangle(roi_color,(ex2,ey2),(ex2+ew2,ey2+eh2),(0,0,0),2)
    print (ex2,ey2,ew2,eh2)
    crop_img1 = roi_color[ey2:ey2+eh2,ex2:ex2+ew2]
    cv2.imwrite("/Users/sonifamily/Desktop/image2.jpg",crop_img1)
    
        #crop_img = img[ey:ey+eh,ex:ex+ew]
        


cap.release()
cv2.destroyAllWindows()
