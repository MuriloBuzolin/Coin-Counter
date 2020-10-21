import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas3.jpeg')
#img = cv.medianBlur(img,15)
img = cv.resize(img, (900, 700))

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
ret1, thresh1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)


cv.imshow('img', img)
cv.imshow('aaaa', thresh)
cv.imshow('bbbbbb', thresh1)



cv.waitKey()
cv.destroyAllWindows()