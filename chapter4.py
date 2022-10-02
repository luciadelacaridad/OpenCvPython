import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)
img[:] = 255, 0, 0 #BGR
print(img)

cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
cv.rectangle(img,(0,0),(250,350),(0,255,0),-1) #en thickness -1 te lo rellena
cv.circle(img,(400,50),30,(255,255,0),cv.FILLED)
cv.putText(img,"LUCIA",(300,200),cv.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv.imshow("Image", img)
cv.waitKey(0)
