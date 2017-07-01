#WEBCAM REALTIME READ
import cv2
import  numpy as np
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,5.0,(640,480))#vary fps depending on th required speed


#0=webcam1
#1=webcam2

while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#creates a frame with gray layer)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    out.write(frame)#opens the gray frame declared earlier with title gray
    if cv2.waitKey(2) & 0xFF==ord('q'):#if wait key is not declared the frame is opened but not seen.
        break

cap.release()
out.release()
cv2.destroyAllWindows()