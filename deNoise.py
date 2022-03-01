import numpy as np
import cv2
from matplotlib import pyplot as plt
from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT

class DeNoise(Toplevel):


    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.denoised_image = None

        self.denoise_button = Button(master=self, text="Remove Noise")
        self.cancel_button = Button(master=self, text="Cancel")
        self.apply_button = Button(master=self, text="Apply")

        self.denoise_button.bind("<ButtonRelease>", self.denoise_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.denoise_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack()

    def denoise_button_released(self, event):
        self.denoise()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.denoised_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.denoised_image)

    def show_image(self):
        self.master.image_viewer.show_image(img=self.denoised_image)

    def denoise(self):
        img5 = cv2.resize(self.original_image, (960, 540))

        dst = cv2.fastNlMeansDenoisingColored(self.original_image, None, 10, 10, 7, 21)

        #self.denoised_image = cv2.resize(dst, (960, 540))
        self.denoised_image = dst

    def close(self):
        self.destroy()