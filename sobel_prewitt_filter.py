import cv2
import numpy as np

def stack(*args):
    return np.hstack(args)

img = cv2.imread('./photos/GrayPhoto.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (3,3), 0)

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
img_prewitt = img_prewittx + img_prewitty



cv2.imshow("Original Image",img)
cv2.imshow("Prewittx", img_prewittx)
cv2.imshow("Prewitty", img_prewitty)

cv2.waitKey(0)
cv2.destroyAllWindows()




