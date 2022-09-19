import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BLUR
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# CANNY EDGES
canny = cv.Canny(blur, 125, 175)
cv.imshow('CANNY', canny)

# Dilanting the images
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('dilated', dilated)

# Erode
erode = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('erode', erode)

# resize
resized = cv.resize(img, (1000, 1000), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resized)

# cropped
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
