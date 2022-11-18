import cv2
import matplotlib.pyplot as plt
import numpy as np

def stack(*args):
    return np.hstack(args)

def rescale(photo):
    s = photo.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)

def gamma_donusumu(r,c,gamma):
    r=r.astype(float)
    s=c*r**gamma
    s=rescale(s)
    return s

photo = cv2.imread("./photos/knee.jpg", 0)
c=1
gamma_values = [3.0,4.0,5.0]
gamma_photos = []
for gamma in gamma_values:
    gamma_photo = gamma_donusumu(photo, c=c,gamma=gamma)
    gamma_photos.append(gamma_photo)

line1 = stack(photo, gamma_photos[0])
line2 = stack(*gamma_photos[1:])

grid = np.vstack((line1,line2))

plt.imshow(grid, cmap="gray")
plt.show()