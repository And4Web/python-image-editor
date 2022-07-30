import cv2

image = cv2.imread("sample.png")
cv2.imshow("this is processed image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()