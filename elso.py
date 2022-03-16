import cv2

img = cv2.imread("Resources/lena.png")


cv2.imshow("Léna képe", img)
cv2.waitKey(0)