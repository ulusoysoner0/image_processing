import cv2
import matplotlib.pyplot as plt
import numpy as np

def photo_negative(photo):
    L = np.max(photo)
    negative_photo = L - photo
    return negative_photo

photo = cv2.imread("./photos/brain.jpg", 0)
negative_photo = photo_negative(photo)

side_by_side = np.hstack((photo, negative_photo))

plt.imshow(side_by_side, cmap="gray")
plt.show()