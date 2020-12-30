import cv2
import numpy as np

#load colored image
img_1 = cv2.imread("Images\\sunflower.png", 1)

#load grayscale image
img_2 = cv2.imread("Images\\sunflower.png", 0)

#resizing images
resized_img_1 = cv2.resize(img_1, (int(img_1.shape[1]/2), int(img_1.shape[0]/2)))

#printing images' shape(dimension)
print(img_1.shape)
print(img_2.shape)

#displaying the loaded images
cv2.imshow("Colored Image", img_1)
cv2.imshow("Grayscale Image", img_2)
cv2.imshow("Resized Image", resized_img_1)

cv2.waitKey(0)
#cv2.waitKey(2000)
cv2.destroyAllWindows()

