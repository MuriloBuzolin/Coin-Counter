import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas2.jpeg',0)
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

#circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT,50,120, param1=500, param2=500, minRadius=50,maxRadius=120)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT,1,200, param1=100, param2=30, minRadius=60,maxRadius=100)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),2)
    
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()