import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

#cv.findContours(img, contours.method,aproximation.method)
"""contours.method
cv.RETR_LIST = todos los contornos 
cv.RETR_TREE = all the contours that are in a hierarchical system
cv.RETR_EXTERNAL = contornos externos """
""" aproximation.method
cv.CHAIN_APPROX_NONE = null
cv.CHAIN_APPROX_SIMPLE = simplifica los contornos """

print(f'{len(contours)} contours found')

cv.waitKey(0)
