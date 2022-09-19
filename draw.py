import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# Importante poner el shape 3 que indica el numero de canales
cv.imshow('Blank', blank)

""" # Pintar la imagen de cierto color
# verde
blank[:] = 0, 255, 0
cv.imshow('Green', blank)

# rojo
blank[:] = 0, 0, 255
cv.imshow('Red', blank)

# porcion de imagen de azul
blank[200:300, 300:400] = 255, 0, 0
cv.imshow('Portion', blank) """

""" cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=2)
#rectangle(img, point1, point2, color, thickness)
cv.imshow('Rectangle', blank)

# Reescalar el rectangulo con las diemnsiones de la imagen
cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('rect', blank) """

""" # CIRCULOS
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
          40, (0, 0, 255), thickness=3)
#cv.circle(img, originpoint, radius, color, thickness)
cv.imshow('circle', blank)

# circulo con relleno
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
          40, (0, 0, 255), thickness=-1)
cv.imshow('circle', blank)

 """

""" # lineas
cv.line(blank, (0, 0),
        (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('line', blank)
 """

cv.putText(blank, 'GAAAA', (255, 255),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)
