import cv2
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image

cb_img = cv2.imread('checkerboard_18x18.png', 0)
print(cb_img)
plt.imshow(cb_img)
plt.show()


