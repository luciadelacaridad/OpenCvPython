import cv2 as cv
import numpy as np

img = cv.imread("Resources/cards.jpg")

width, height = 250, 350 #tamaño de una carta
pts1 = np.float32([[327,170],[520,215],[207,339],[440,391]]) #puntos en la imagen
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #puntos en la realidad
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgOutput = cv.warpPerspective(img, matrix, (width,height))

cv.imshow("Image",img)
cv.imshow("Output",imgOutput)
cv.waitKey(0)