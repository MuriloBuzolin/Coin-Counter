import cv2
import numpy as np

img_inicial = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas2.jpeg')
img_inicial = cv2.cvtColor(img_inicial, cv2.COLOR_BGR2GRAY)
img_agr = cv2.Canny(img_inicial, 150, 400, 5)

gray = cv2.medianBlur(cv2.cvtColor(img_agr, cv2.COLOR_RGB2GRAY), 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=50, minRadius=50, maxRadius=100)
circles = np.uint16(np.around(circles))

mask = np.full((img_agr.shape[0], img_agr.shape[1]), 0, dtype=np.uint8)
for i in circles[0, :]:
    cv2.circle(mask, (i[0], i[1]), i[2], (255, 255, 255), -1)

fg = cv2.bitwise_or(img_agr, img_agr, mask=mask)
mask = cv2.bitwise_not(mask)
background = np.full(img_agr.shape, 255, dtype=np.uint8)
bk = cv2.bitwise_or(background, background, mask=mask)

final = cv2.bitwise_or(fg, bk)

cv2.imshow('img_agr', img_agr)
cv2.imshow('fg', fg)
cv2.imshow('final', final)
cv2.imshow('bk', bk)

cv2.waitKey(0)
cv2.destroyAllWindows
