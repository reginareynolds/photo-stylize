from tkinter import Tk
from tkinter.filedialog import askopenfilename


def file_prompt():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


if __name__ == '__main__':
    file = askopenfilename()
