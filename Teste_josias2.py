import cv2
import numpy as np
import matplotlib 

img = cv2.imread('C:\\Users\\MURILO\\Desktop\\Python2\\Projeto_Cofrinho\\Moedas1.jpeg')
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,th1 = cv2.threshold(img_cinza, 127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img_cinza,127, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2 )
th3 = cv2.adaptiveThreshold(img_cinza,127, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155,2 )

cv2.imshow('imath1gem', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)

cv2.waitKey()
cv2.destroyAllWindows()
