import cv2 as cv
import math
import numpy as np
from . import helper as hp


def averageFilter(path, m_path):
	img = cv.imread(path, 3)
	row, col, ch = img.shape
	mask = np.loadtxt(m_path)
	row_mask, col_mask = mask.shape

	inc = row_mask // 2
	r_ext, g_ext, b_ext = hp.createExtendedMatrixes(img, inc)
	np.savetxt("./assets/red_extended_matrix.txt", r_ext, fmt="%s")
	np.savetxt("./assets/green_extended_matrix.txt", g_ext, fmt="%s")
	np.savetxt("./assets/blue_extended_matrix.txt", b_ext, fmt="%s")
	r_matrix, g_matrix, b_matrix = hp.createRGBMatrixes(row, col)

	for i in range(row):
		for j in range(col):
			red_pixel = 0
			green_pixel = 0
			blue_pixel = 0
			for x in range(row_mask):
				for y in range(col_mask):
					# print('Pointer: ',r_ext[i+x, j+y])
					# print('Mask: ', mask[x,y])
					red_pixel += r_ext[i+x, j+y] * mask[x, y]
					green_pixel += g_ext[i+x, j+y] * mask[x, y]
					blue_pixel += b_ext[i+x, j+y] * mask[x, y]
			# print('New pointer red: ', red_pixel)
			# print('New pointer green: ', green_pixel)
			# print('New pointer blue: ', blue_pixel)
			r_matrix[i, j] = red_pixel
			g_matrix[i, j] = green_pixel
			b_matrix[i, j] = blue_pixel
	avImage = cv.merge([r_matrix, g_matrix, b_matrix])
	hp.showImage('Average', avImage)

	

def medianFilter(path, mask):
	img=cv.imread(path, 3)
	print(img)
