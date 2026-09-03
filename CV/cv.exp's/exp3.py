import cv2
image=cv2.imread("pic.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,100,200)
cv2.imshow("or",image)
cv2.imshow("cc",edge)
cv2.waitKey(0)
cv2.destoryALLWindows()
