import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas3.jpeg', 0)
        #img1_teste = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas3.jpeg',0)
img = cv2.medianBlur(img,5)
        #img1_teste = cv2.medianBlur(img1_teste,5)
#img = cv2.resize(img, (1280,928))   #entra com 1280p 928p
        #img1 = cv2.resize(img1, (900,750))
print(img.shape)


th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
#th4_teste = cv2.adaptiveThreshold(img1_teste,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            #cv2.THRESH_BINARY,11,1.1)


circles = cv2.HoughCircles( th3, cv2.HOUGH_GRADIENT,1,80, param1=100, param2=30, minRadius=35,maxRadius=65)
        #circless = cv2.HoughCircles( th4_teste, cv2.HOUGH_GRADIENT,1,80, param1=100, param2=30, minRadius=35,maxRadius=65)
circles = np.uint16(np.around(circles))
        #circless = np.uint16(np.around(circless))



for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),-1)
    
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),2)



        #img1_teste = cv2.resize(img1_teste, (900,750))
img = cv2.resize(img, (900,750))
        #th4_teste = cv2.resize(th4_teste, (900,750))
th3 = cv2.resize(th3, (900,750))

cv2.imshow('img', img)
        #cv2.imshow('img1_teste', img1_teste)
cv2.imshow('th3', th3)
        #cv2.imshow('th4_teste', th4_teste)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
