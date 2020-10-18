from tkinter import Tk
from tkinter import Button, Frame
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np


class Menu(Tk):
    def __init__(self, title, buttons):
        # Final variables
        self.path = None
        self.orig_img = None
        self.stand_grad = None

        # CREATE MENU ITEMS

        # CONFIGURE MENU
        Tk.__init__(self)
        # Bind keys to functions
        self.bind('<Return>', self.onclick)

        # Set window title
        self.title(title)
        self.frame = Frame(self)

        # Create buttons
        self.buttons = buttons  # Button click history
        self.rows = []  # Array to store button locations
        index = 2
        for button in self.buttons:
            self.button = Button(self, text=button[1], command=lambda response=button[0]: self.onclick(response))
            self.button.grid(row=index, column=0, padx=5, pady=3, sticky="W E")
            self.rows.append(self.button)
            index = index + 1

            # Disable buttons until file is selected
            if index-3 == 0:
                pass
            else:
                self.button['state'] = 'disabled'

        # # Return to menu or close program
        # self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # TODO: Reset button text and disable buttons if user closes out of file prompt.
    # Enable submission on selection of file
    def enable(self):
        # File has been selected
        if self.path != self.buttons[0][1]:
            for button in self.rows:
                button['state'] = 'normal'
        else:  # File not selected yet
            pass

    # noinspection PyUnusedLocal
    def onclick(self, response):
        # User selected button with mouse
        if type(response) == int:
            pass
        # User selected button with keyboard
        else:
            index = 1
            for location in self.rows:
                if self.focus_get() == location:
                    response = index
                else:
                    pass
                index = index + 1

        choice = 'func_' + str(response)
        method = getattr(self, choice)
        return method()

    # Enable menu option opening and closing
    @staticmethod
    def hide(frame):
        frame.withdraw()

    @staticmethod
    def show(frame):
        frame.update()
        frame.deiconify()

    # File prompt
    def func_1(self):
        # Hide menu
        self.hide(self)

        # Create prompt for file
        self.path = file_prompt()
        self.rows[0].config(text=self.path)
        self.enable()
        self.show(self)

    # Standardize gradient
    def func_2(self):
        # Hide menu
        self.hide(self)

        standardize_gradient(self.path)
    # def on_closing(self):
    #     ans = tkMessageBox.askokcancel('Verify exit', "Do you really want to quit the program?")
    #     if ans:
    #         self.quit()
    #         sys.exit(3)
    #     else:
    #         pass


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
    menu = Menu("Main menu", ((1, "Select an image."),
                              (2, "Standardize gradient")))
    # menu.eval('tk::PlaceWindow %s center' % menu.winfo_pathname(menu.winfo_id()))
    menu.mainloop()
    menu.destroy()

    # TODO: Figure out why eval expression isn't working
