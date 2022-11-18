import cv2
import matplotlib.pyplot as plt
import numpy as np

def log_donusumu(r,c):
    r=r.astype(float)
    s=c*np.log(1+r)
    s=rescale(s)
    return s

def stack(*args):
    return np.hstack(args)

def rescale(photo):
    s = photo.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)

photo = cv2.imread("./photos/fourier_spectrum.tif", 0)
log_photo = log_donusumu(photo,c=1)

side_by_side = stack(photo,log_photo)

plt.imshow(side_by_side, cmap="gray")
plt.show()