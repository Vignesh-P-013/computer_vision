import cv2
image=cv2.imread("pic.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("OI",image)
cv2.imshow("gr",gray)
cv2.waitKey(0)
cv2.destoryALLWindows()
                  
