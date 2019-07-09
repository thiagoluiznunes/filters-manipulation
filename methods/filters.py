import sys
import cv2
import math


def test():
    print('hellooo')


def thresholding(path, measure):
    img = cv2.imread(path, 0)
    newImg = img
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if img[i, j] < 50:
                newImg[i, j] = 0
            else:
                newImg[i, j] = 255
                
    cv2.startWindowThread()
    cv2.imshow('Thresholding', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
