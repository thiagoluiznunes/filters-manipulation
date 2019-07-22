from PIL import Image
import numpy as np
import cv2 as cv


def clear_matrix(matrix):
	newMatrix = matrix
	for i in range(len(matrix)):
		for x in range(len(matrix[0])):
			newMatrix[i][x] = 0
	return newMatrix


def show_image(method, img):
	im = Image.fromarray(img)
	im.show()


def create_rgb_matrixes(row, col):
	r_matrix = np.zeros((row, col), dtype=np.uint8)
	g_matrix = np.zeros((row, col), dtype=np.uint8)
	b_matrix = np.zeros((row, col), dtype=np.uint8)
	return r_matrix, g_matrix, b_matrix


def create_yiq_matrixes(row, col):
	y_matrix = np.zeros((row, col))
	i_matrix = np.zeros((row, col))
	q_matrix = np.zeros((row, col))
	return y_matrix, i_matrix, q_matrix


def create_extended_matrixes(img, inc):
	row, col, ch = img.shape

	r_extended = np.zeros((row + inc * 2, col + inc * 2), dtype=np.uint8)
	g_extended = np.zeros((row + inc * 2, col + inc * 2), dtype=np.uint8)
	b_extended = np.zeros((row + inc * 2, col + inc * 2), dtype=np.uint8)

	for i in range(row):
		for j in range(col):
			b_extended[i + inc, j + inc] = img[i, j, 0]
			g_extended[i + inc, j + inc] = img[i, j, 1]
			r_extended[i + inc, j + inc] = img[i, j, 2]
	return r_extended, g_extended, b_extended

def rebate_mask(mask):
	return np.rot90(np.rot90(mask))

def zeroOr255(value, measure):
	if value < measure:
		return 0
	else:
		return 255
