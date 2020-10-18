from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import os


def file_prompt():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def standardize_gradient(file):
    # Read image
    original_image = cv2.imread(file, 0)
    stylized_image = np.copy(original_image)

    # TODO: Make this a slider
    scale = int(input("Choose how much you want to reduce the gradient"))

    cv2.imshow("Original", original_image)

    limit = 0
    while limit < 255:
        group = np.where((original_image[:, :]>=limit) & (original_image[:, :]<=limit+scale))
        stylized_image[group] = (limit+(255/scale))//2
        limit = limit+scale

    cv2.imshow("Standardized gradient", stylized_image)
    cv2.waitKey(0)


if __name__ == '__main__':
    path = os.path.normpath(file_prompt())

    standardize_gradient(path)

    # TODO: Create menu to choose between different stylization options
