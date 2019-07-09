# import strformat
import sys
import cv2
import math
import numpy as np
from methods import filters

def main():
    """Função principal da aplicação.
    """
    filters.thresholding(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
