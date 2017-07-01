import  numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('frontalface.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
cap = cv2.VideoCapture(0)
watch_cascade = cv2.CascadeClassifier('watch-cascade.xml')
while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    watches = watch_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in watches:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color =img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,225,0),2)
    cv2.imshow('gray',gray)
    cv2.imshow('img',img)
    if cv2.waitKey(3) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
