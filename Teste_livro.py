import cv2
import numpy as np

img_inicial = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas2.jpeg')
#retval, threshold = cv2.threshold(img_inicial, 100, 220, cv2.THRESH_BINARY)

#cv2.imshow('threshold', threshold)

img_cinza = cv2.cvtColor(img_inicial, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(img_cinza, 100, 220, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(img_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
retval2, otsu = cv2.threshold(img_cinza, 255, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
img_agr = cv2.Canny(otsu, 150, 400, 5)

cv2.imshow('img_agr', img_agr)
cv2.imshow('otsu', otsu)
#cv2.imshow('gaus', gaus)
#cv2.imshow('threshold2', threshold2)


cv2.waitKey(0)
cv2.destroyAllWindows