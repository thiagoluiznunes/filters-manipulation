import sys
import cv2
import math
import numpy as np
from tkinter.filedialog import askopenfilename
from methods import filters


def main():
	"""Filter Manipulation.
	"""
	print('Filter Manipulation Tool')
	print('')
	print('Choose one operation bellow:')
	print('')
	print('1. Thresholding Filter')
	print('2. RGB Filter')
	print('3. Convert RGB to YIQ')
	print('4. Negative filter')
	print('')
	option = input()
	filename = askopenfilename()

	if option == "1":
		print('Enter a measurement between 0 and 255')
		measure = input()
		print('Choose image type:')
		print('1. Monochromatic')
		print('2. Colorful')
		imgType = input()
		filters.thresholding(filename, measure, imgType)
	elif option == "2":
		print('1. Read')
		print('2. Green')
		print('3. Blue')
		color = input()
		if color == "1":
			filters.showRGB(filename, 'read')
		elif color == "2":
			filters.showRGB(filename, 'green')
		else:
			filters.showRGB(filename, 'blue')
	elif option == "3":
		filters.rbgToYIQ(filename)
	elif option == "4":
		filters.negative(filename)
	else:
		print('Closed!')


if __name__ == '__main__':
	main()
