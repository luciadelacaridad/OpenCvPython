import cv2 as cv
import numpy as np

img = cv.imread("Resources/lucia.JPG")
print(img.shape)

imgResize = cv.resize(img,(300,300)) #primero width y despues height
imgCropped = img[0:250,125:375] #primero height y despues width


cv.imshow("Image Resized",imgResize)
cv.imshow("Image Cropped", imgCropped)
cv.waitKey(0)