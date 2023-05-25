import cv2

img = cv2.imread("S__86515719_2.jpg")

point1 = (160,430)
point2 = (270,560)

cv2.rectangle(img,point1,point2,color=(0,255,0),thickness=5)
cv2.imshow("me",img)
cv2.waitKey(0)