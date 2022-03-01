

from PIL import Image, ImageOps
from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT
import cv2  # for image processing


class BorderFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.bordered_image = self.master.processed_image

        self.r_label = Label(self, text="R")
        self.r_scale = Scale(self, from_=0, to_=255, length=250, resolution=1,
                             orient=HORIZONTAL)
        self.g_label = Label(self, text="G")
        self.g_scale = Scale(self, from_=0, to_=255, length=250, resolution=1,
                             orient=HORIZONTAL)
        self.b_label = Label(self, text="B")
        self.b_scale = Scale(self, from_=0, to_=255, length=250, resolution=1,
                             orient=HORIZONTAL)

        #        self.border_button = Button(master=self, text="Border")
        self.apply_button = Button(master=self, text="Apply")
        self.preview_button = Button(self, text="Preview")
        self.cancel_button = Button(master=self, text="Cancel")

        #       self.border_button.bind("<ButtonRelease>", self.border_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.preview_button.bind("<ButtonRelease>", self.show_button_release)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        #       self.border_button.pack()
        self.r_label.pack()
        self.r_scale.pack()
        self.g_label.pack()
        self.g_scale.pack()
        self.b_label.pack()
        self.b_scale.pack()
        self.cancel_button.pack(side=RIGHT)
        self.preview_button.pack(side=RIGHT)
        self.apply_button.pack()

    #   def border_button_released(self, event):
    #       self.border()
    #       self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.bordered_image
        self.show_image()
        self.close()

    def show_button_release(self, event):

        b, g, r = cv2.split(self.bordered_image)

        for b_value in b:
            cv2.add(b_value, self.b_scale.get(), b_value)
        for g_value in g:
            cv2.add(g_value, self.g_scale.get(), g_value)
        for r_value in r:
            cv2.add(r_value, self.r_scale.get(), r_value)

        ReSized1 = cv2.resize(self.original_image, (960, 540))

        color = [b, g, r]
        constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=color)

        self.bordered_image = cv2.resize(constant, (960, 540))

        # self.bordered_image = cv2.merge((b, g, r))
        self.show_image(self.bordered_image)

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self, img=None):
        self.master.image_viewer.show_image(img=img)

    #    def border(self):
    #       ReSized1 = cv2.resize(self.original_image, (960, 540))
    #        #imgBorder = ImageOps.expand(ReSized1, border=100, fill='red')

    #        white = [255, 255, 255]
    #       constant = cv2.copyMakeBorder(ReSized1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=white)

    #       self.bordered_image = cv2.resize(constant, (960, 540))

    def close(self):
        self.show_image()
        self.destroy()




white = [255,255,255]
img12 = cv2.imread('img1.jpg')
constant= cv2.copyMakeBorder(img12,20,20,20,20,cv2.BORDER_CONSTANT,value=white)
#cv2.imwrite('output.png',constant)


# Open images and store them in a list
images = [Image.open(x) for x in ['img1.jpg', 'img2.jpg', 'img3.jpg']]
total_width = 0
max_height = 0
# find the width and height of the final image
for img in images:
    total_width += img.size[0]
    max_height = max(max_height, img.size[1])
# create a new image with the appropriate height and width
new_img = Image.new('RGB', (total_width, max_height))
# Write the contents of the new image
current_width = 0
for img in images:
  new_img.paste(img, (current_width,0))
  current_width += img.size[0]
# Save the image
#new_img.save('NewImage.jpg')


