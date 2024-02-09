import cv2 as cv
import numpy as np 
img=cv.imread(r"D:\Coding\UAS\7.jpeg")
img=cv.resize(img,None,fx=0.9,fy=0.9)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=255-gray
ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
contours, hierarchy=cv.findContours(binary, mode=cv.RETR_TREE, method =cv.CHAIN_APPROX_NONE)
print("Length of contours{}".format(len(contours)))
print(contours)
imgcopy=img.copy()
cv.drawContours(imgcopy, contours, -1, (0, 255, 0), 2)
cv.imshow("Grayscale Image",gray)
cv.imshow("Drawn Contours",imgcopy)
cv.imshow("binary Image",binary)
cv.waitKey(0)
cv.destroyAllWindows()
