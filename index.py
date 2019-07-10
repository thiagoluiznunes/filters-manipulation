import sys
import cv2
import math
import numpy as np
from methods import filters


def main():
	"""Filter Manipulation.
	"""
	print('Filter Manipulation Tool')
	print('')
	print('Choose one operation bellow!')
	print('')
	print('1. Thresholding Filter')
	print('2. RGB Filter')
	print('3. Convert RGB to YIQ')
	print('')
	option = input()

	if option == "1":
		filters.thresholding(sys.argv[1], sys.argv[2])
	elif option == "2":
		print('1. Read')
		print('2. Green')
		print('3. Blue')
		color = input()
		if color == "1":
			filters.showRGB(sys.argv[1], 'read')
		elif color == "2":
			filters.showRGB(sys.argv[1], 'green')
		else:
			filters.showRGB(sys.argv[1], 'blue')
	elif option == "3":
		filters.convertToYIQ(sys.argv[1])

	else:
		print('Closed!')


if __name__ == '__main__':
	main()
