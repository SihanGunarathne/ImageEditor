from PIL import Image, ImageOps
from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT
import cv2  # for image processing

class BorderFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.bordered_image = None

        self.white_button = Button(master=self, text="white")
        self.red_button = Button(master=self, text="Red")
        self.green_button = Button(master=self, text="Green")
        self.black_button = Button(master=self, text="Black")
        self.blue_button = Button(master=self, text="Blue")
        self.yellow_button = Button(master=self, text="Yellow")
        self.aqua_button = Button(master=self, text="Aqua")
        self.magenta_button = Button(master=self, text="Magenta")
        self.gray_button = Button(master=self, text="Gray")
        self.maroon_button = Button(master=self, text="Maroon")
        self.cancel_button = Button(master=self, text="Cancel")
        self.apply_button = Button(master=self, text="Apply")

        self.white_button.bind("<ButtonRelease>", self.white_button_released)
        self.red_button.bind("<ButtonRelease>", self.red_button_released)
        self.green_button.bind("<ButtonRelease>", self.green_button_released)
        self.black_button.bind("<ButtonRelease>", self.black_button_released)
        self.blue_button.bind("<ButtonRelease>", self.blue_button_released)
        self.yellow_button.bind("<ButtonRelease>", self.yellow_button_released)
        self.aqua_button.bind("<ButtonRelease>", self.aqua_button_released)
        self.magenta_button.bind("<ButtonRelease>", self.magenta_button_released)
        self.gray_button.bind("<ButtonRelease>", self.gray_button_released)
        self.maroon_button.bind("<ButtonRelease>", self.maroon_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.white_button.pack()
        self.red_button.pack()
        self.green_button.pack()
        self.black_button.pack()
        self.blue_button.pack()
        self.yellow_button.pack()
        self.aqua_button.pack()
        self.magenta_button.pack()
        self.gray_button.pack()
        self.maroon_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack()

    def white_button_released(self, event):
        self.white()
        self.show_image()

    def red_button_released(self, event):
        self.red()
        self.show_image()

    def green_button_released(self, event):
        self.green()
        self.show_image()

    def black_button_released(self, event):
        self.black()
        self.show_image()

    def blue_button_released(self, event):
        self.blue()
        self.show_image()

    def yellow_button_released(self, event):
        self.yellow()
        self.show_image()

    def aqua_button_released(self, event):
        self.aqua()
        self.show_image()

    def magenta_button_released(self, event):
        self.magenta()
        self.show_image()

    def gray_button_released(self, event):
        self.gray()
        self.show_image()

    def maroon_button_released(self, event):
        self.maroon()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.bordered_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.bordered_image)

    def white(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        whiteColor = [255, 255, 255]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=whiteColor)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def red(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        redColor = [0, 0, 255]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=redColor)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def green(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        Color = [0, 128, 0]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=Color)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def black(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        Color = [0, 0, 0]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=Color)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def blue(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        Color = [255, 0, 0]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=Color)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def yellow(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        Color = [0, 255, 255]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=Color)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def aqua(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        Color = [255, 255, 0]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=Color)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def magenta(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        Color = [255, 0, 255]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=Color)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def gray(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        Color = [128, 128, 128]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=Color)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def maroon(self):
        ReSized1 = cv2.resize(self.original_image, (960, 540))
        Color = [0, 0, 128]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=Color)
        self.bordered_image = cv2.resize(constant, (960, 540))

    def close(self):
        self.destroy()
