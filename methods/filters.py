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
	im = Image.fromarray(img)
	im.show()


def createRGBMatrixes(row, col):
	r_matrix = np.zeros((row, col), dtype=np.uint8)
	g_matrix = np.zeros((row, col), dtype=np.uint8)
	b_matrix = np.zeros((row, col), dtype=np.uint8)
	return r_matrix, g_matrix, b_matrix


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

	r_matrix, g_matrix, b_matrix = createRGBMatrixes(row, col)

	for x in range(0, row):
		for j in range(0, col):
			y = y_matrix[x, j]
			i = i_matrix[x, j]
			q = q_matrix[x, j]
			# YIQ to RGB
			r_matrix[x, j] = abs((1.000 * y) + (0.956 * i) + (0.621 * q))
			g_matrix[x, j] = abs((1.000 * y) - (0.272 * i) - (0.647 * q))
			b_matrix[x, j] = abs((1.000 * y) - (1.106 * i) + (1.703 * q))

	rgb_img = cv.merge([r_matrix, g_matrix, b_matrix])
	showImage('RGB to YIQ to RGB', rgb_img)


def rbgToYIQ(path):
	y_matrix, i_matrix, q_matrix = convertToYIQ(path)
	convertToRGB(y_matrix, i_matrix, q_matrix)


def negative(path, option):
	img = cv.imread(path, 3)
	row, col, ch = img.shape

	if option == '1':
		blue, green, red = cv.split(img)
		r_matrix, g_matrix, b_matrix = createRGBMatrixes(row, col)
		for i in range(row):
			for j in range(col):
				r_matrix[i, j] = 255 - red[i, j]
				g_matrix[i, j] = 255 - green[i, j]
				b_matrix[i, j] = 255 - blue[i, j]
		negativeImage = cv.merge([r_matrix, g_matrix, b_matrix])
		showImage('Image Negative', negativeImage)

	elif option == '2':
		y_matrix, i_matrix, q_matrix = convertToYIQ(path)
		for i in range(row):
		    for j in range(col):
		        y_matrix[i, j] = 255 - y_matrix[i, j]
		negativeImage = cv.merge([y_matrix, i_matrix, q_matrix])
		cv.imshow('Image Negative', negativeImage)
		cv.waitKey(0)
		cv.destroyAllWindows()

	else:
		y_matrix, i_matrix, q_matrix = convertToYIQ(path)
		for i in range(row):
			for j in range(col):
				y_matrix[i, j] = 255 - y_matrix[i, j]
		convertToRGB(y_matrix, i_matrix, q_matrix)


def brightnessHandler(path, measure, option):
	img = cv.imread(path, 3)
	row, col, ch = img.shape
	blue, green, red = cv.split(img)
	measure = int(measure)

	r_matrix, g_matrix, b_matrix = createRGBMatrixes(row, col)

	if option == 'add':
		for i in range(row):
			for j in range(col):
				newRed = red[i, j] + measure
				newGreen = green[i, j] + measure
				newBlue = blue[i, j] + measure
				if newRed > 255:
					r_matrix[i, j] = 255
				else:
					r_matrix[i, j] = newRed
				if newGreen > 255:
					g_matrix[i, j] = 255
				else:
					g_matrix[i, j] = newGreen
				if newBlue > 255:
					b_matrix[i, j] = 255
				else:
					b_matrix[i, j] = newBlue
	else:
		y_matrix, i_matrix, q_matrix = convertToYIQ(path)
		for i in range(row):
			for j in range(col):
				newRed = abs(red[i, j] * measure)
				newGreen = abs(green[i, j] * measure)
				newBlue = abs(blue[i, j] * measure)
				if newRed > 255:
					r_matrix[i, j] = 255
				else:
					r_matrix[i, j] = newRed
				if newGreen > 255:
					g_matrix[i, j] = 255
				else:
					g_matrix[i, j] = newGreen
				if newBlue > 255:
					b_matrix[i, j] = 255
				else:
					b_matrix[i, j] = newBlue
		for i in range(row):
			for j in range(col):
				newY = y_matrix[i, j] * measure
				if newY > 255:
					y_matrix[i, j] = 255
				else:
					y_matrix[i, j] = newY

	brightnessImage = cv.merge([r_matrix, g_matrix, b_matrix])
	showImage('Brightness Image', brightnessImage)
	convertToRGB(y_matrix, i_matrix, q_matrix)

def thresholding(path, measure, option):
	if option == "1":
		img = cv.imread(path, 0)
		row, col = img.shape
		thImage = np.zeros((row, col))

		for i in range(row):
			for j in range(col):
				if img[i, j] < int(measure):
					thImage[i, j] = 0
				else:
					thImage[i, j] = 255
		showImage('Thresholding', thImage)
	else:
		img = cv.imread(path, 3)
		row, col, ch = img.shape

		r_matrix, g_matrix, b_matrix = createRGBMatrixes(row, col)

		for i in range(row):
			for j in range(col):
				if img[i, j, 0] < int(measure):
					r_matrix[i, j] = 0
				if img[i, j, 1] < int(measure):
					g_matrix[i, j] = 0
				if img[i, j, 2] < int(measure):
					b_matrix[i, j] = 0
				if img[i, j, 0] >= int(measure):
					r_matrix[i, j] = 255
				if img[i, j, 1] >= int(measure):
					g_matrix[i, j] = 255
				if img[i, j, 2] >= int(measure):
					b_matrix[i, j] = 255

		thImage = cv.merge([r_matrix, g_matrix, b_matrix])
		showImage('Thresholding', thImage)


def thresholdingY(path, choose, measure):
	img = cv.imread(path, 3)
	row, col, ch = img.shape
	y_matrix, i_matrix, q_matrix = convertToYIQ(path)
	if choose == "1":
		for i in range(row):
			for j in range(col):
				if y_matrix[i,j] < int(measure):
					y_matrix[i,j] = 0
				else:
					y_matrix[i,j] = 255
		threY = cv.merge([y_matrix, i_matrix, q_matrix])
		cv.imshow('Thresholding Y measure', threY)
		cv.waitKey(0)
		cv.destroyAllWindows()
	else:
		count = 0
		for i in range(row):
			for j in range(col):
				count += y_matrix[i,j]
		count /= row * col
		for i in range(row):
			for j in range(col):
				if y_matrix[i,j] < count:
					y_matrix[i,j] = 0
				else:
					y_matrix[i,j] = 255
		threY = cv.merge([y_matrix, i_matrix, q_matrix])
		cv.imshow('Thresholding Y average', threY)
		cv.waitKey(0)
		cv.destroyAllWindows()
