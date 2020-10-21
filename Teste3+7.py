import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas1.jpeg',0)
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
#contorno = cv.Canny(cimg, 150, 400, 5)

#circles = cv.HoughCircles(contorno, cv.HOUGH_GRADIENT,73,80, param1=20, param2=250, minRadius=50,maxRadius=120)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT,1,200, param1=100, param2=30, minRadius=60,maxRadius=100)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # Circulo
    cv.circle(cimg,(i[0],i[1]),i[2],(255,255,25),4)
    #cv.circle(contorno,(i[0],i[1]),i[2],(255,25,255),4)
    # Centro
    cv.circle(cimg,(i[0],i[1]),2,(25,255,25),2)
    #cv.circle(contorno,(i[0],i[1]),2,(255,25,255),2)


#cv.imshow('contorno circles',contorno)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()