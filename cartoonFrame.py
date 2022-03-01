from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT
import cv2  # for image processing

class CartoonFrame(Toplevel):

    #def cartoonify(self, event):
        # read the image
       # originalmage = cv2.imread(original_image)
       # originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)
        # print(image)  # image is stored in form of numbers

        # confirm that image is chosen
      #  if originalmage is None:
      #      print("Can not find any image. Choose appropriate file")
       #     sys.exit()



    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.cartooned_image = None

        self.cartoon_button = Button(master=self, text="Cartoon")
        self.cancel_button = Button(master=self, text="Cancel")
        self.apply_button = Button(master=self, text="Apply")

        self.cartoon_button.bind("<ButtonRelease>", self.cartoon_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.cartoon_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack()


    def cartoon_button_released(self, event):
        self.cartoon()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.cartooned_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.cartooned_image)

    def cartoon(self):

        ReSized1 = cv2.resize(self.original_image, (960, 540))

        # converting an image to grayscale
        grayScaleImage = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        ReSized2 = cv2.resize(grayScaleImage, (960, 540))

        # applying median blur to smoothen an image
        smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
        ReSized3 = cv2.resize(smoothGrayScale, (960, 540))

        # retrieving the edges for cartoon effect
        # by using thresholding technique
        getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                        cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 9, 9)

        ReSized4 = cv2.resize(getEdge, (960, 540))

        # applying bilateral filter to remove noise
        # and keep edge sharp as required
        colorImage = cv2.bilateralFilter(self.original_image, 9, 300, 300)
        ReSized5 = cv2.resize(colorImage, (960, 540))

        # masking edged image with our "BEAUTIFY" image
        cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)

        ReSized6 = cv2.resize(cartoonImage, (960, 540))


        self.cartooned_image = cv2.resize(cartoonImage, (960, 540))

    def close(self):
        self.destroy()
