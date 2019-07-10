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

	def convert_y(r, g, b):
		return (r * 0.299) + (g * 0.587) + (b * 0.114)
	def convert_i(r, g, b):
		return (r * 0.596) - (g * 0.274) - (b * 0.332)
	def convert_q(r, g, b):
		return (r * 0.211) - (g * 0.523) - (b * 0.312)

	img = cv2.imread(path, 3)
	blue, green, red = cv2.split(img)

	y_matrix = np.zeros((blue.shape[0], blue.shape[1]))
	i_matrix = np.zeros((blue.shape[0], blue.shape[1]))
	q_matrix = np.zeros((blue.shape[0], blue.shape[1]))

	for i in range(0, 2):
		for j in range(0, 2):
			y_matrix[i,j] = convert_y(blue[i,j], green[i,j], red[i,j])
			i_matrix[i,j] = convert_i(blue[i,j], green[i,j], red[i,j])
			q_matrix[i,j] = convert_q(blue[i,j], green[i,j], red[i,j])

	# YIQ_image = cv2.merge([y_matrix, i_matrix, q_matrix])
	showImage('YIQ Image', q_matrix)
	# print('Y MATRIX', y_matrix)
	# print('')
	# print('I MATRIX', i_matrix)
	# print('')
	# print('Q MATRIX', q_matrix)
	# return y_matrix, i_matrix, q_matrix

def convertToRGB(y_matrix, i_matrix, q_matrix):

	r_matrix = y_matrix
	g_matrix = y_matrix
	b_matrix = y_matrix

	def convert_red(y, i, q) : return (1.000 * y) + (0.956 * i) + (0.621 * q)
	def convert_green(y, i, q) : return (1.000 * y) - (0.272 * i) - (0.647 * q)
	def convert_blue(y, i, q) : return (1.000 * y) - (1.106 * i) + (1.703 * q)

	for i in range(0, y_matrix.shape[0]):
		for j in range(0, y_matrix.shape[1]):
			r_matrix[i,j] = convert_red(y_matrix[i,j], i_matrix[i,j], q_matrix[i,j])
			g_matrix[i,j] = convert_red(y_matrix[i,j], i_matrix[i,j], q_matrix[i,j])
			b_matrix[i,j] = convert_red(y_matrix[i,j], i_matrix[i,j], q_matrix[i,j])
	showImage('RED BAND', r_matrix)

def rgbTIQrgb(path):
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
