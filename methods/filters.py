import sys
import cv2 as cv
import math
import numpy as np
from PIL import Image


def clearMatrix(matrix):
    newMatrix = matrix
    for i in range(len(matrix)):
        for x in range(len(matrix[0])):
            newMatrix[i][x] = 0
    return newMatrix


def showImage(method, img):
    # cv.startWindowThread()
    # cv.imshow(method, img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
	im = Image.fromarray(img)
	im.show()


def showRGB(path, band):
    img = cv.imread(path, 3)
    blue, green, red = cv.split(img)

    if band == 'blue':
        green = clearMatrix(green)
        red = clearMatrix(red)
        imgBlue = cv.merge([blue, green, red])
        showImage('Blue', imgBlue)
    elif band == 'green':
        blue = clearMatrix(blue)
        red = clearMatrix(red)
        imgGreen = cv.merge([blue, green, red])
        showImage('Green', imgGreen)
    else:
        blue = clearMatrix(blue)
        green = clearMatrix(green)
        imgRed = cv.merge([blue, green, red])
        showImage('Red', imgRed)


def convertToYIQ(path):
    img = cv.imread(path, 3)
    row, col, ch = img.shape
    blue, green, red = cv.split(img)

    y_matrix = np.zeros((row, col))
    i_matrix = np.zeros((row, col))
    q_matrix = np.zeros((row, col))

    for i in range(row):
        for j in range(col):
            r = red[i, j]
            g = green[i, j]
            b = blue[i, j]
            # RGB to YIQ
            y_matrix[i, j] = (0.299 * r) + (0.587 * g) + (0.114 * b)
            i_matrix[i, j] = (0.596 * r) - (0.274 * g) - (0.322 * b)
            q_matrix[i, j] = (0.211 * r) - (0.523 * g) + (0.312 * b)

    return y_matrix, i_matrix, q_matrix


def convertToRGB(y_matrix, i_matrix, q_matrix):
    row = y_matrix.shape[0]
    col = y_matrix.shape[1]

    r_matrix = np.zeros((row, col), dtype=np.uint8)
    g_matrix = np.zeros((row, col), dtype=np.uint8)
    b_matrix = np.zeros((row, col), dtype=np.uint8)

    for x in range(0, row):
        for j in range(0, col):
            y = y_matrix[x, j]
            i = i_matrix[x, j]
            q = q_matrix[x, j]
            # YIQ to RGB
            r_matrix[x, j] = abs((1.000 * y) + (0.956 * i) + (0.621 * q))
            g_matrix[x, j] = abs((1.000 * y) - (0.272 * i) - (0.647 * q))
            b_matrix[x, j] = abs((1.000 * y) - (1.106 * i) + (1.703 * q))

    # rgb_img = cv.merge([b_matrix, g_matrix, r_matrix])
    rgb_img = cv.merge([r_matrix, g_matrix, b_matrix])
    showImage('RGB to YIQ to RGB', rgb_img)


def rbgToYIQ(path):
    y_matrix, i_matrix, q_matrix = convertToYIQ(path)
    convertToRGB(y_matrix, i_matrix, q_matrix)

def negative(path):
	img = cv.imread(path, 3)
	row, col, ch = img.shape
	blue, green, red = cv.split(img)

	r_matrix = np.zeros((row, col), dtype=np.uint8)
	g_matrix = np.zeros((row, col), dtype=np.uint8)
	b_matrix = np.zeros((row, col), dtype=np.uint8)
	
	for i in range(row):
		for j in range(col):
			r_matrix[i,j] = 255 - red[i,j]
			g_matrix[i,j] = 255 - green[i,j]
			b_matrix[i,j] = 255 - blue[i,j]

	negativeImage = cv.merge([r_matrix, g_matrix, b_matrix])
	showImage('Image Negative', negativeImage)

def thresholding(path, measure):
    img = cv.imread(path, 0)
    newImg = img
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] < 50:
                newImg[i,j] = 0
            else:
                newImg[i,j] = 255
    showImage('Thresholding', newImg)
