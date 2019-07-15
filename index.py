import sys
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
	print('3. Convert RGB to YIQ to RGB')
	print('4. Negative Filter')
	print('5. Incriese Brightness')
	print('6. Multiply Brightness')
	print('7. Thresholding Filter in Y')
	print('')
	option = input()
	filename = askopenfilename()

	if option == "1":
		print('Enter a measurement between 0 and 255:')
		measure = input()
		print('Choose image type:')
		print('1. Monochromatic')
		print('2. Colorful')
		imgType = input()
		filters.thresholding(filename, measure, imgType)
	elif option == "2":
		print('1. Red')
		print('2. Green')
		print('3. Blue')
		color = input()
		if color == "1":
			filters.showRGB(filename, 'red')
		elif color == "2":
			filters.showRGB(filename, 'green')
		elif color == "3":
			filters.showRGB(filename, 'blue')
	elif option == "3":
		filters.rgbYIQrgb(filename)
	elif option == "4":
		print('1. RGB')
		print('2. YIQ')
		print('3. RGB YIQ RGB')
		measure = input()
		filters.negative(filename, measure)
	elif option == "5":
		print('Enter a incriese measurement:')
		measure = input()
		filters.brightnessHandler(filename, measure, 'add')
	elif option == "6":
		print('Enter a multiply measurement:')
		measure = input()
		filters.brightnessHandler(filename, measure, 'multiply')
	elif option == "7":
		print('1. Measure')
		print('2. Average')
		choose = input()
		if choose == '1':
			print('Enter a measurement between 0 and 255:')
			measure = input()
			filters.thresholdingY(filename, choose, measure)
		else:
			filters.thresholdingY(filename, choose, 'measure')

	else:
		print('Closed!')


if __name__ == '__main__':
	main()
