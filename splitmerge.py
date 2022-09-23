import cv2 as cv
import numpy as np

img = cv.imread('Photos/Park.jpg')
cv.imshow('Boston', img)

b, g, r = cv.split(img)

# nos entrega los canales de colores, pero en grayscale
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

merged = cv.merge([b, g, r])
cv.imshow('merge', merged)

# para poder ver los canales de colores tenemos que reconstruir la imagenes
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('cblue', blue)
cv.imshow('cgreeen', green)
cv.imshow('cred', red)

cv.waitKey(0)
