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
	blue, green, red = cv2.split(img)

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


def convertToYIQ(path):
	img = cv2.imread(path, 3)
	height, width, channel = img.shape
	blue, green, red = cv2.split(img)

	# myread = np.full((height, width), 25)
	y_matrix = np.full((height, width), 0)
	i_matrix = np.full((height, width), 0)
	q_matrix = np.full((height, width), 0)

	for i in range(0, height):
		for j in range(0, width):
			r = red[i,j]
			g = green[i,j]
			b = blue[i,j]

			#RGB to YIQ
			y_matrix[i,j] = (0.299 * r) + (0.587 * g) + (0.114 * b)
			i_matrix[i,j] = (0.596 * r) - (0.274 * g) - (0.322 * b)
			q_matrix[i,j] = (0.211 * r) - (0.523 * g) + (0.312 * b)

	YIQ_image = cv2.merge([q_matrix, i_matrix, y_matrix])
	print('RED PURE', red)
	print('')
	print('GREEN PURE', green)
	print('')
	print('BLUE PURE', blue)
	print('')
	print('')
	print('')
	print('')
	# showImage('YIQ Image', q_matrix)
	return y_matrix, i_matrix, q_matrix

def convertToRGB(y_matrix, i_matrix, q_matrix):
	height = y_matrix.shape[0]
	width = y_matrix.shape[1]

	r_matrix = np.full((height, width), 0)
	print('Y', y_matrix)
	print('')
	print('I', i_matrix)
	print('')
	print('Q', q_matrix)
	print('')
	g_matrix = np.full((height, width), 0)
	b_matrix = np.full((height, width), 0)

	for x in range(0, height):
		for j in range(0, width):
			y = y_matrix[x,j]
			i = i_matrix[x,j]
			q = q_matrix[x,j]

			#YIQ to RGB
			r_matrix[x,j] = (1.000 * y) + (0.956 * i) + (0.621 * q)
			g_matrix[x,j] = (1.000 * y) - (0.272 * i) - (0.647 * q)
			b_matrix[x,j] = (1.000 * y) - (1.106 * i) + (1.703 * q)
	# print('RED NEW', r_matrix)
	# showImage('YIQ Image', r_matrix)

def rbgToYIQ(path):
	y_matrix, i_matrix, q_matrix = convertToYIQ(path)
	convertToRGB(y_matrix, i_matrix, q_matrix)


def thresholding(path, measure):
	img = cv2.imread(path, 0)
	newImg = img
	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			if img[i,j] < 50:
				newImg[i,j] = 0
			else:
				newImg[i,j] = 255
	showImage('Thresholding', newImg)
