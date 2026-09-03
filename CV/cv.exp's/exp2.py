import cv2
image=cv2.imread("pic.jpg")
blur=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("or",image)
cv2.imshow("Blur",blur)
cv2.waitKey(0)
cv2.destoryALLWindows()
