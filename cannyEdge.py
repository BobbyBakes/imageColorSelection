#doing all the relevant imports
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Read in the image and convert to grayscale
image = mpimg.imread('image/road3.png')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Define a kernel size for Gaussian smoothing / blurring
# Note: this step is optional as cv2.Canny() applies a 5x5 Gaussian internally
kernel_size = 3
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)
blur_grayCopy = np.uint8(blur_gray)

# Define parameters for Canny and run it
# NOTE: if you try running this code you might want to change these!
low_threshold = 0
high_threshold = 1000000
edges = cv2.Canny(blur_grayCopy, low_threshold, high_threshold)

# Display the image
plt.imshow(edges, cmap='Greys_r')
plt.show()