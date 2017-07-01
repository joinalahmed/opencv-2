import numpy as np
import cv2

img = cv2.imread('bird.png',cv2.IMREAD_COLOR)
cv2.line(img, (0,0) ,(150,150) ,(225,152,30))
#                (coordinates)   (b,g,r)

cv2.rectangle(img,(15,25), (200,150),(55,35,12), 2)
cv2.circle(img,(50,50),15,(55,35,12),-102)
pts = np.array([[10,5],[20,30],[35,15],[70,20]],np.int32)
pts = pts.reshape((-1,2,1))#resizes it to a 1x2 matrix
cv2.polylines(img,[pts],True,(0,255,0),2)#True(isclosed)indicates that the initial and final pts are connected

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'Hello World',(0,130),font,3,(255,255,255))
cv2.imwrite('draw.png',img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()