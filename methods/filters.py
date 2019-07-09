import sys
import cv2
import math
import numpy as np

def clearMatrix(matrix):
	newMatrix = matrix
	for i in range(len(matrix)):
		for x in range(len(matrix[0])):
			newMatrix[i][x] = 0
	return newMatrix

def showImage(method, img):
	cv2.startWindowThread()
	cv2.imshow(method, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def showRGB(path, band):
	img = cv2.imread(path, 3)
	blue,green,red = cv2.split(img) 
	
	if band == 'blue':
		green = clearMatrix(green)
		red = clearMatrix(red)
		imgBlue = cv2.merge([blue, green, red])
		showImage('Blue', imgBlue)
	elif band == 'green':
		blue = clearMatrix(blue)
		red = clearMatrix(red)
		imgGreen = cv2.merge([blue, green, red])
		showImage('Green', imgGreen)
	else:
		blue = clearMatrix(blue)
		green = clearMatrix(green)
		imgRed = cv2.merge([blue, green, red])
		showImage('Red', imgRed)

def thresholding(path, measure):
    img = cv2.imread(path, 0)
    newImg = img
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if img[i, j] < 50:
                newImg[i, j] = 0
            else:
                newImg[i, j] = 255
    showImage('Thresholding', newImg)
