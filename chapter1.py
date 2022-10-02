import cv2 as cv
print("Package Imported")

img = cv.imread("Resources/lucia.JPG")

cv.imshow("Output",img)
cv.waitKey(0)