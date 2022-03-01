from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT
import cv2  # for image processing
import numpy as np

class BgRemove(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.bgremoved_image = None

        self.bgremove_button = Button(master=self, text="Remove Background")
        self.addbg1_button = Button(master=self, text="Background1")
        self.addbg2_button = Button(master=self, text="Background2")
        self.addbg3_button = Button(master=self, text="Background3")
        self.addbg4_button = Button(master=self, text="Background4")
        self.cancel_button = Button(master=self, text="Cancel")
        self.apply_button = Button(master=self, text="Apply")

        self.bgremove_button.bind("<ButtonRelease>", self.bgremove_button_released)
        self.addbg1_button.bind("<ButtonRelease>", self.addbg1_button_released)
        self.addbg2_button.bind("<ButtonRelease>", self.addbg2_button_released)
        self.addbg3_button.bind("<ButtonRelease>", self.addbg3_button_released)
        self.addbg4_button.bind("<ButtonRelease>", self.addbg4_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.bgremove_button.pack()
        self.addbg1_button.pack()
        self.addbg2_button.pack()
        self.addbg3_button.pack()
        self.addbg4_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack()


    def bgremove_button_released(self, event):
        self.bgremove()
        self.show_image()

    def addbg1_button_released(self, event):
        self.addbg1()
        self.show_image()

    def addbg2_button_released(self, event):
        self.addbg2()
        self.show_image()

    def addbg3_button_released(self, event):
        self.addbg3()
        self.show_image()

    def addbg4_button_released(self, event):
        self.addbg4()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.bgremoved_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.bgremoved_image)

    def bgremove(self):
        image1 = cv2.resize(self.original_image, (960, 540))
       # show('Input image', image)
        # blur the image to smmooth out the edges a bit, also reduces a bit of noise
        blurred = cv2.GaussianBlur(image1, (5, 5), 0)
        # convert the image to grayscale
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        # apply thresholding to conver the image to binary format
        # after this operation all the pixels below 200 value will be 0...
        # and all th pixels above 200 will be 255
        ret, gray = cv2.threshold(gray, 220, 255, cv2.CHAIN_APPROX_NONE)

        image2 = gray.astype(np.uint8)
        contours, hierarchy = cv2.findContours(
            image2,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)

        # find the largest contour area in the image
        contour = largest_contour
        image_contour = np.copy(image1)
        cv2.drawContours(image_contour, [contour], 0, (0, 255, 0), 2, cv2.LINE_AA, maxLevel=2)
        #show('Contour', image_contour)


        # create a black `mask` the same size as the original grayscale image
        mask = np.zeros_like(gray)
        # fill the new mask with the shape of the largest contour
        # all the pixels inside that area will be white
        cv2.fillPoly(mask, [contour], 255)
        # create a copy of the current mask
        res_mask = np.copy(mask)
        res_mask[mask == 0] = cv2.GC_BGD  # obvious background pixels
        res_mask[mask == 255] = cv2.GC_PR_BGD  # probable background pixels
        res_mask[mask == 255] = cv2.GC_FGD  # obvious foreground pixels

        # create a mask for obvious and probable foreground pixels
        # all the obvious foreground pixels will be white and...
        # ... all the probable foreground pixels will be black
        mask2 = np.where(
            (res_mask == cv2.GC_FGD) | (res_mask == cv2.GC_PR_FGD),
            255,
            0
        ).astype('uint8')

        # create `new_mask3d` from `mask2` but with 3 dimensions instead of 2
        new_mask3d = np.repeat(mask2[:, :, np.newaxis], 3, axis=2)
        mask3d = new_mask3d
        mask3d[new_mask3d > 0] = 255.0
        mask3d[mask3d > 255] = 255.0
        # apply Gaussian blurring to smoothen out the edges a bit
        # `mask3d` is the final foreground mask (not extracted foreground image)
        mask3d = cv2.GaussianBlur(mask3d, (5, 5), 0)
       # show('Foreground mask', mask3d)

        # create the foreground image by zeroing out the pixels where `mask2`...
        # ... has black pixels
        foreground = np.copy(image1).astype(float)
        foreground[mask2 == 0] = 0


        # save the images to disk
       # save_name = args['input'].split('/')[-1].split('.')[0]
       # cv2.imwrite(f"outputs/{save_name}_foreground.png", foreground)
       # cv2.imwrite(f"outputs/{save_name}_foreground_mask.png", mask3d)
        #cv2.imwrite(f"outputs/{save_name}_contour.png", image_contour)

        #cv2.imwrite("foreground.png", foreground)
        self.bgremoved_image = cv2.resize(foreground.astype(np.uint8), (960, 540))

    def addbg1(self):
        image1 = cv2.resize(self.original_image, (960, 540))
        # show('Input image', image)
        # blur the image to smmooth out the edges a bit, also reduces a bit of noise
        blurred = cv2.GaussianBlur(image1, (5, 5), 0)
        # convert the image to grayscale
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        # apply thresholding to conver the image to binary format
        # after this operation all the pixels below 200 value will be 0...
        # and all th pixels above 200 will be 255
        ret, gray = cv2.threshold(gray, 200, 255, cv2.CHAIN_APPROX_NONE)

        image2 = gray.astype(np.uint8)
        contours, hierarchy = cv2.findContours(
            image2,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)

        # find the largest contour area in the image
        contour = largest_contour
        image_contour = np.copy(image1)
        cv2.drawContours(image_contour, [contour], 0, (0, 255, 0), 2, cv2.LINE_AA, maxLevel=2)
        # show('Contour', image_contour)

        # create a black `mask` the same size as the original grayscale image
        mask = np.zeros_like(gray)
        # fill the new mask with the shape of the largest contour
        # all the pixels inside that area will be white
        cv2.fillPoly(mask, [contour], 255)
        # create a copy of the current mask
        res_mask = np.copy(mask)
        res_mask[mask == 0] = cv2.GC_BGD  # obvious background pixels
        res_mask[mask == 255] = cv2.GC_PR_BGD  # probable background pixels
        res_mask[mask == 255] = cv2.GC_FGD  # obvious foreground pixels

        # create a mask for obvious and probable foreground pixels
        # all the obvious foreground pixels will be white and...
        # ... all the probable foreground pixels will be black
        mask2 = np.where(
            (res_mask == cv2.GC_FGD) | (res_mask == cv2.GC_PR_FGD),
            255,
            0
        ).astype('uint8')

        # create `new_mask3d` from `mask2` but with 3 dimensions instead of 2
        new_mask3d = np.repeat(mask2[:, :, np.newaxis], 3, axis=2)
        mask3d = new_mask3d
        mask3d[new_mask3d > 0] = 255.0
        mask3d[mask3d > 255] = 255.0
        # apply Gaussian blurring to smoothen out the edges a bit
        # `mask3d` is the final foreground mask (not extracted foreground image)
        mask3d = cv2.GaussianBlur(mask3d, (5, 5), 0)
        # show('Foreground mask', mask3d)

        # create the foreground image by zeroing out the pixels where `mask2`...
        # ... has black pixels
        foreground = np.copy(image1).astype(float)
        foreground[mask2 == 0] = 0

        # normalization of mask3d mask, keeping values between 0 and 1
        mask3d = mask3d / 255.0
        # get the scaled product by multiplying
        foreground = cv2.multiply(mask3d, foreground)
        # read the new background image
        background = cv2.imread('input/background1.jpg')
        # resize it according to the foreground image
        background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))
        background = background.astype(np.float)
        # get the scaled product by multiplying
        background = cv2.multiply(1.0 - mask3d, background)
        # add the foreground and new background image
        new_image = cv2.add(foreground, background)

        #show('New image', new_image.astype(np.uint8))
        #cv2.imwrite(f"outputs/{save_name}_new_background.jpg", new_image)

        self.bgremoved_image = cv2.resize(new_image.astype(np.uint8), (960, 540))

    def addbg2(self):
        image1 = cv2.resize(self.original_image, (960, 540))
        blurred = cv2.GaussianBlur(image1, (5, 5), 0)
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        ret, gray = cv2.threshold(gray, 200, 255, cv2.CHAIN_APPROX_NONE)

        image2 = gray.astype(np.uint8)
        contours, hierarchy = cv2.findContours(
            image2,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)

        # find the largest contour area in the image
        contour = largest_contour
        image_contour = np.copy(image1)
        cv2.drawContours(image_contour, [contour], 0, (0, 255, 0), 2, cv2.LINE_AA, maxLevel=2)
        # show('Contour', image_contour)

        # create a black `mask` the same size as the original grayscale image
        mask = np.zeros_like(gray)
        cv2.fillPoly(mask, [contour], 255)
        # create a copy of the current mask
        res_mask = np.copy(mask)
        res_mask[mask == 0] = cv2.GC_BGD  # obvious background pixels
        res_mask[mask == 255] = cv2.GC_PR_BGD  # probable background pixels
        res_mask[mask == 255] = cv2.GC_FGD  # obvious foreground pixels

        mask2 = np.where(
            (res_mask == cv2.GC_FGD) | (res_mask == cv2.GC_PR_FGD),
            255,
            0
        ).astype('uint8')

        # create `new_mask3d` from `mask2` but with 3 dimensions instead of 2
        new_mask3d = np.repeat(mask2[:, :, np.newaxis], 3, axis=2)
        mask3d = new_mask3d
        mask3d[new_mask3d > 0] = 255.0
        mask3d[mask3d > 255] = 255.0
        mask3d = cv2.GaussianBlur(mask3d, (5, 5), 0)
        # show('Foreground mask', mask3d)

        # create the foreground image by zeroing out the pixels where `mask2`...
        # ... has black pixels
        foreground = np.copy(image1).astype(float)
        foreground[mask2 == 0] = 0

        # normalization of mask3d mask, keeping values between 0 and 1
        mask3d = mask3d / 255.0
        # get the scaled product by multiplying
        foreground = cv2.multiply(mask3d, foreground)
        # read the new background image
        background = cv2.imread('input/background2.jpg')
        # resize it according to the foreground image
        background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))
        background = background.astype(np.float)
        # get the scaled product by multiplying
        background = cv2.multiply(1.0 - mask3d, background)
        # add the foreground and new background image
        new_image = cv2.add(foreground, background)

        self.bgremoved_image = cv2.resize(new_image.astype(np.uint8), (960, 540))

    def addbg3(self):
        image1 = cv2.resize(self.original_image, (960, 540))
        blurred = cv2.GaussianBlur(image1, (5, 5), 0)
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        ret, gray = cv2.threshold(gray, 200, 255, cv2.CHAIN_APPROX_NONE)

        image2 = gray.astype(np.uint8)
        contours, hierarchy = cv2.findContours(
            image2,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)

        # find the largest contour area in the image
        contour = largest_contour
        image_contour = np.copy(image1)
        cv2.drawContours(image_contour, [contour], 0, (0, 255, 0), 2, cv2.LINE_AA, maxLevel=2)
        # show('Contour', image_contour)

        # create a black `mask` the same size as the original grayscale image
        mask = np.zeros_like(gray)
        cv2.fillPoly(mask, [contour], 255)
        # create a copy of the current mask
        res_mask = np.copy(mask)
        res_mask[mask == 0] = cv2.GC_BGD  # obvious background pixels
        res_mask[mask == 255] = cv2.GC_PR_BGD  # probable background pixels
        res_mask[mask == 255] = cv2.GC_FGD  # obvious foreground pixels

        mask2 = np.where(
            (res_mask == cv2.GC_FGD) | (res_mask == cv2.GC_PR_FGD),
            255,
            0
        ).astype('uint8')

        # create `new_mask3d` from `mask2` but with 3 dimensions instead of 2
        new_mask3d = np.repeat(mask2[:, :, np.newaxis], 3, axis=2)
        mask3d = new_mask3d
        mask3d[new_mask3d > 0] = 255.0
        mask3d[mask3d > 255] = 255.0
        mask3d = cv2.GaussianBlur(mask3d, (5, 5), 0)
        # show('Foreground mask', mask3d)

        # create the foreground image by zeroing out the pixels where `mask2`...
        # ... has black pixels
        foreground = np.copy(image1).astype(float)
        foreground[mask2 == 0] = 0

        # normalization of mask3d mask, keeping values between 0 and 1
        mask3d = mask3d / 255.0
        # get the scaled product by multiplying
        foreground = cv2.multiply(mask3d, foreground)
        # read the new background image
        background = cv2.imread('input/background3.jpg')
        # resize it according to the foreground image
        background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))
        background = background.astype(np.float)
        # get the scaled product by multiplying
        background = cv2.multiply(1.0 - mask3d, background)
        # add the foreground and new background image
        new_image = cv2.add(foreground, background)

        self.bgremoved_image = cv2.resize(new_image.astype(np.uint8), (960, 540))

    def addbg4(self):
        image1 = cv2.resize(self.original_image, (960, 540))
        blurred = cv2.GaussianBlur(image1, (5, 5), 0)
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        ret, gray = cv2.threshold(gray, 200, 255, cv2.CHAIN_APPROX_NONE)

        image2 = gray.astype(np.uint8)
        contours, hierarchy = cv2.findContours(
            image2,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)

        # find the largest contour area in the image
        contour = largest_contour
        image_contour = np.copy(image1)
        cv2.drawContours(image_contour, [contour], 0, (0, 255, 0), 2, cv2.LINE_AA, maxLevel=2)
        # show('Contour', image_contour)

        # create a black `mask` the same size as the original grayscale image
        mask = np.zeros_like(gray)
        cv2.fillPoly(mask, [contour], 255)
        # create a copy of the current mask
        res_mask = np.copy(mask)
        res_mask[mask == 0] = cv2.GC_BGD  # obvious background pixels
        res_mask[mask == 255] = cv2.GC_PR_BGD  # probable background pixels
        res_mask[mask == 255] = cv2.GC_FGD  # obvious foreground pixels

        mask2 = np.where(
            (res_mask == cv2.GC_FGD) | (res_mask == cv2.GC_PR_FGD),
            255,
            0
        ).astype('uint8')

        # create `new_mask3d` from `mask2` but with 3 dimensions instead of 2
        new_mask3d = np.repeat(mask2[:, :, np.newaxis], 3, axis=2)
        mask3d = new_mask3d
        mask3d[new_mask3d > 0] = 255.0
        mask3d[mask3d > 255] = 255.0
        mask3d = cv2.GaussianBlur(mask3d, (5, 5), 0)
        # show('Foreground mask', mask3d)

        # create the foreground image by zeroing out the pixels where `mask2`...
        # ... has black pixels
        foreground = np.copy(image1).astype(float)
        foreground[mask2 == 0] = 0

        # normalization of mask3d mask, keeping values between 0 and 1
        mask3d = mask3d / 255.0
        # get the scaled product by multiplying
        foreground = cv2.multiply(mask3d, foreground)
        # read the new background image
        background = cv2.imread('input/background4.jpg')
        # resize it according to the foreground image
        background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))
        background = background.astype(np.float)
        # get the scaled product by multiplying
        background = cv2.multiply(1.0 - mask3d, background)
        # add the foreground and new background image
        new_image = cv2.add(foreground, background)

        self.bgremoved_image = cv2.resize(new_image.astype(np.uint8), (960, 540))

    def close(self):
        self.destroy()
