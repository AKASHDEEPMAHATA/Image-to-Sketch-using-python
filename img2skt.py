step 1 : install the module opencv-python
step 2 : start coding




import cv2

image = cv2.imread('msd final6.jpg') # loads an image from the file explorer

# convert an image from one color space to another
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(grey_img) # helps in masking of the image

# sharp edges in images are smoothed while minimizing too much blurring
blur = cv2.GaussianBlur(invert, (21, 21), 0)

invertedblur = cv2.bitwise_not(blur)

sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("msd.png", sketch) # converted image is saved as mentioned name
