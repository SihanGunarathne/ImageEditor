from PIL import Image , ImageDraw , ImageFont, ImageTk
from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT
import cv2  # for image processing
from matplotlib import pyplot as plt

class TextEdit(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.texted_image = None

        self.text1_button = Button(master=self, text="Happy Birthday")
        self.text2_button = Button(master=self, text="ThankYou")
        self.text3_button = Button(master=self, text="Happy New Year")
        self.text4_button = Button(master=self, text="Merry Christmas")
        self.text5_button = Button(master=self, text="Happy Valentines day")
        self.text6_button = Button(master=self, text="Welcome")
        self.cancel_button = Button(master=self, text="Cancel")
        self.apply_button = Button(master=self, text="Apply")

        self.text1_button.bind("<ButtonRelease>", self.text1_button_released)
        self.text2_button.bind("<ButtonRelease>", self.text2_button_released)
        self.text3_button.bind("<ButtonRelease>", self.text3_button_released)
        self.text4_button.bind("<ButtonRelease>", self.text4_button_released)
        self.text5_button.bind("<ButtonRelease>", self.text5_button_released)
        self.text6_button.bind("<ButtonRelease>", self.text6_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.text1_button.pack()
        self.text2_button.pack()
        self.text3_button.pack()
        self.text4_button.pack()
        self.text5_button.pack()
        self.text6_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack()


    def text1_button_released(self, event):
        self.text1()
        self.show_image()

    def text2_button_released(self, event):
        self.text2()
        self.show_image()

    def text3_button_released(self, event):
        self.text3()
        self.show_image()

    def text4_button_released(self, event):
        self.text4()
        self.show_image()

    def text5_button_released(self, event):
        self.text5()
        self.show_image()

    def text6_button_released(self, event):
        self.text6()
        self.show_image()


    def apply_button_released(self, event):
        self.master.processed_image = self.texted_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.texted_image)

    def text1(self):
        img1 = cv2.resize(self.original_image, (960, 540))

        cv2.putText(img=img1, text='Happy Birthday', org=(150, 250), fontFace=cv2.FONT_ITALIC, fontScale=2,
                    color=(0, 255, 0), thickness=6)
        #plt.imshow(img1)
        self.texted_image = cv2.resize(img1, (960, 540))

    def text2(self):
        img1 = cv2.resize(self.original_image, (960, 540))

        cv2.putText(img=img1, text='Thank You', org=(150, 250), fontFace=cv2.FONT_ITALIC, fontScale=2,
                    color=(128, 255, 128), thickness=6)
        #plt.imshow(img1)
        self.texted_image = cv2.resize(img1, (960, 540))

    def text3(self):
        img1 = cv2.resize(self.original_image, (960, 540))

        cv2.putText(img=img1, text='Happy New Year', org=(150, 250), fontFace=cv2.FONT_ITALIC, fontScale=2,
                    color=(0, 255, 255), thickness=6)
        #plt.imshow(img1)
        self.texted_image = cv2.resize(img1, (960, 540))

    def text4(self):
        img1 = cv2.resize(self.original_image, (960, 540))

        cv2.putText(img=img1, text='Merry Christmas', org=(150, 250), fontFace=cv2.FONT_ITALIC, fontScale=2,
                    color=(0, 0, 255), thickness=6)
        #plt.imshow(img1)
        self.texted_image = cv2.resize(img1, (960, 540))

    def text5(self):
        img1 = cv2.resize(self.original_image, (960, 540))

        cv2.putText(img=img1, text='Happy Valentines day', org=(150, 250), fontFace=cv2.FONT_ITALIC, fontScale=2,
                    color=(0, 0, 255), thickness=6)
        #plt.imshow(img1)
        self.texted_image = cv2.resize(img1, (960, 540))

    def text6(self):
        img1 = cv2.resize(self.original_image, (960, 540))

        cv2.putText(img=img1, text='Welcome', org=(200, 250), fontFace=cv2.FONT_ITALIC, fontScale=4,
                    color=(255, 0, 0), thickness=7)
        #plt.imshow(img1)
        self.texted_image = cv2.resize(img1, (960, 540))

    def close(self):
        self.destroy()












