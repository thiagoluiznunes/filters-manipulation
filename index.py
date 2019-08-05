import sys
from tkinter.filedialog import askopenfilename
from methods import filters as ft
from methods import convolution_filters as conv


def main():
	"""Filter Manipulation.
	"""
	print('')
	print('####### Filter Manipulation Tool by Thiago Luiz Nunes ######')
	print('')
	print('Choose one operation bellow:')
	print('')
	print('1. Thresholding Filter')
	print('2. RGB Filter and GRAY')
	print('3. Convert RGB to YIQ to RGB')
	print('4. Negative Filter')
	print('5. Incriese Brightness')
	print('6. Multiply Brightness')
	print('7. Thresholding Filter in Y')
	print('8. Convolution Average Filter')
	print('9. Convolution Median Filter')
	print('10.Convolution Sobel Filter')
	print('11.SHOW YIQ')
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
		ft.thresholding(filename, measure, imgType)
	elif option == "2":
		print('1. Red')
		print('2. Green')
		print('3. Blue')
		print('4. Gray')
		color = input()
		if color == "1":
			ft.show_rgb(filename, 'red')
		elif color == "2":
			ft.show_rgb(filename, 'green')
		elif color == "3":
			ft.show_rgb(filename, 'blue')
		elif color == "4":
			ft.show_rgb(filename, 'gray')
	elif option == "3":
		ft.rgb_yiq_rgb(filename)
	elif option == "4":
		print('1. RGB')
		print('2. YIQ')
		print('3. RGB YIQ RGB')
		measure = input()
		ft.negative(filename, measure)
	elif option == "5":
		print('Enter a incriese measurement:')
		measure = input()
		ft.brightness_handler(filename, measure, 'add')
	elif option == "6":
		print('Enter a multiply measurement:')
		measure = input()
		ft.brightness_handler(filename, measure, 'multiply')
	elif option == "7":
		print('1. Measure')
		print('2. Average')
		choose = input()
		if choose == '1':
			print('Enter a measurement between 0 and 255:')
			measure = input()
			ft.thresholding_y(filename, choose, measure)
		else:
			ft.thresholding_y(filename, choose, 'measure')
	elif option == "8":
		mask = askopenfilename()
		conv.kernel_filter(filename, mask)
	elif option == "9":
		mask = askopenfilename()
		conv.median_filter(filename, mask)
		# conv.median_filter('assets/images/2817540617.jpg', 'assets/masks/mask5x5.txt')
		# conv.median_filter('assets/images/lena.png', 'assets/masks/mask5x5.txt')
	elif option == "10":
		mask = askopenfilename()
		conv.sobel_filter(filename, mask)
		# conv.sobel_filter('assets/images/CNN1.png', 'assets/masks/sobel-mask.txt')
	elif option == "11":
		ft.show_yiq(filename)
	else:
		print('Closed!')


if __name__ == '__main__':
	main()
