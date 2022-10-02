import cv2 as cv
import numpy as np


def getContours(imagen):
    contours,hierarchy = cv.findContours(imagen, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)  #puntos (x,y) de los contornos sin aproximacion
    for cnt in contours:
        area = cv.contourArea(cnt)                                                        #area de los contornos

        if area > 500: #tenemos en cuenta solo las de area mayor que 500 pixeles
            print(area)
            cv.drawContours(img, cnt, -1, (255, 0, 0), 3)                                 #dibuja los contornos sobre img
            peri = cv.arcLength(cnt,True)                                                 #perimetro de los contornos
            approx = cv.approxPolyDP(cnt,0.02*peri,True)                                  #aproxima el contorno a un poligono con menos vertices
                                                                                          # tal que la distancia entre ellos es menor que la
                                                                                          # precision especificada
            objCor = len(approx)                                                     #numero de vertices del poligono aproximado
            print(objCor)                                                            #imprime el numero de vertices del poligono
            x, y, w, h = cv.boundingRect(approx)                       # puntos iniciales (x,y), anchura y altura del rectangulo que rodea la figura
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # dibuja dicho rectangulo
            if objCor == 3:                                            # condiciones para clasificar los contornos
                objectType = "TRI"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "SQR"
                else:
                    objectType = "RECT"
            elif objCor > 4:
                objectType = "CIRCLE"
            else:
                objectType = "NONE"

            cv.putText(img, objectType, (x+(w//2)-10,y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)


path = "Resources/shapes.jpg"
img = cv.imread(path)
imgCanny = cv.Canny(img,50,50)

getContours(imgCanny) #llamamos a la funcion sobre la imgCanny porque es como se detectan los contornos

cv.imshow("Contour",img)
cv.waitKey(0)
