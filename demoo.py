'''import pandas as pd
import numpy as np

from glob import glob
import cv2 
import matplotlib.pylab as plt

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)

#reading image
img_files = glob('/image/picture.png')

img_mpl = plt.imread(img_files[20])
img_cv2 = plt.imread(img_files[20])

#dimension of array 3 dimensiona (height, width, channels)
img_mpl.shape, img_cv2.shape

pd.Series(img_mpl.flatten()).plot(kind='hist', bins=50, title='Distribution of Pixel Values')
plt.show()

#display image
fig, ax = plt.subplots(figsize=(10,10))
ax.iamshow(img_mpl)
ax.axis('off')
plt.show()
'''