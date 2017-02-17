import os

import matplotlib.pyplot as plt
import matplotlib.image as mpiImg
import numpy as np

image = mpiImg.imread('image/road3.png')
print 'image {0}'.format('road.png')
print 'image type {0}'.format(str(type(image)))
print 'image shape {0}'.format(str(image.shape))

xsize = image.shape[1]
ysize = image.shape[0]

print 'xsize {0}'.format(str(xsize))
print 'ysize {0}'.format(str(ysize))

colorSelect = np.copy(image)

red = .5
green = .5
blue = .5
rgb_threshold = [red, green, blue]

thresholds = (image[:, :, 0] < rgb_threshold[0]) \
             | (image[:, :, 1] < rgb_threshold[1]) \
             | (image[:, :, 2] < rgb_threshold[2])

colorSelect[thresholds] = [0, 0, 0]

plt.imshow(colorSelect)
plt.show()


# With a region
regionSelect = np.copy(image)

leftBotton = [0, 539]
rightBotton = [900, 300]
apextBotton = [400, 0]
