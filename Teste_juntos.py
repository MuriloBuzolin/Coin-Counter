import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas3.jpeg',0)
#img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (900, 700))
img = cv2.medianBlur(img,7)

#gaus = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 1)
gaus2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 5)
ret, thresh = cv2.threshold(gaus2,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

circles = cv2.HoughCircles(gaus2, cv2.HOUGH_GRADIENT,1,200, param1=100, param2=30, minRadius=60,maxRadius=100)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),2)
    
cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.imshow('circles', circles)
#cv2.imshow('gaus2', gaus2)

cv2.waitKey()
cv2.destroyAllWindows()