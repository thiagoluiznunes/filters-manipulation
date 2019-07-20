import cv2 as cv
import math
import numpy as np
from . import helper as hp


def kernelFilter(path, mask_path):
    img = cv.imread(path, 3)
    row, col, ch = img.shape
    mask = hp.rebateMask(np.loadtxt(mask_path))
    row_mask, col_mask = mask.shape

    inc = row_mask // 2
    r_ext, g_ext, b_ext = hp.createExtendedMatrixes(img, inc)
    r_matrix, g_matrix, b_matrix = hp.createRGBMatrixes(row, col)

    for i in range(row):
        for j in range(col):
            red_pixel = 0
            green_pixel = 0
            blue_pixel = 0
            for x in range(row_mask):
                for y in range(col_mask):
                    red_pixel += r_ext[i+x, j+y] * mask[x, y]
                    green_pixel += g_ext[i+x, j+y] * mask[x, y]
                    blue_pixel += b_ext[i+x, j+y] * mask[x, y]
            r_matrix[i, j] = red_pixel
            g_matrix[i, j] = green_pixel
            b_matrix[i, j] = blue_pixel
    kernelImage = cv.merge([r_matrix, g_matrix, b_matrix])
    hp.showImage('Kernel Filter', kernelImage)

    np.savetxt("./assets/files/red_extended_matrix.txt", r_ext, fmt="%s")
    np.savetxt("./assets/files/green_extended_matrix.txt", g_ext, fmt="%s")
    np.savetxt("./assets/files/blue_extended_matrix.txt", b_ext, fmt="%s")
    np.savetxt("./assets/files/red_final_matrix.txt", r_matrix, fmt="%s")
    np.savetxt("./assets/files/green_final_matrix.txt", g_matrix, fmt="%s")
    np.savetxt("./assets/files/blue_final_matrix.txt", b_matrix, fmt="%s")


def medianFilter(path, mask):
    img = cv.imread(path, 3)
    row, col, ch = img.shape
    mask = hp.rebateMask(np.loadtxt(mask))
    row_mask, col_mask = mask.shape

    inc = row_mask // 2
    r_ext, g_ext, b_ext = hp.createExtendedMatrixes(img, inc)
    r_matrix, g_matrix, b_matrix = hp.createRGBMatrixes(row, col)

    for i in range(row):
        for j in range(col):
            red_aux = np.array(r_ext[i:i+row_mask, j:j+col_mask]).flatten()
            green_aux = np.array(g_ext[i:i+row_mask, j:j+col_mask]).flatten()
            blue_aux = np.array(g_ext[i:i+row_mask, j:j+col_mask]).flatten()

            r_matrix[i, j] = red_aux[row_mask // 2]
            g_matrix[i, j] = green_aux[row_mask // 2]
            b_matrix[i, j] = blue_aux[row_mask // 2]
            # print(np.sort(red_aux))
            # print(red_aux[row_mask // 2])
            # print(np.sort(green_aux))
            # print(np.sort(blue_aux))
    medianImage = cv.merge([r_matrix, g_matrix, b_matrix])
    hp.showImage('Median Filter', medianImage)
