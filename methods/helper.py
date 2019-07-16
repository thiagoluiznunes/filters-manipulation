from PIL import Image
import numpy as np
import cv2 as cv


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


def createYIQMatrixes(row, col):
    y_matrix = np.zeros((row, col))
    i_matrix = np.zeros((row, col))
    q_matrix = np.zeros((row, col))
    return y_matrix, i_matrix, q_matrix


def createExtendedMatrixes(img, inc):
    row, col, ch = img.shape

    r_extended = np.zeros((row + inc, col + inc), dtype=np.uint8)
    g_extended = np.zeros((row + inc, col + inc), dtype=np.uint8)
    b_extended = np.zeros((row + inc, col + inc), dtype=np.uint8)


    for i in range(row):
        for j in range(col):
            b_extended[i + inc, j + inc] = img[i, j, 0]
            g_extended[i + inc, j + inc] = img[i, j, 1]
            r_extended[i + inc, j + inc] = img[i, j, 2]
    return r_extended, g_extended, b_extended
