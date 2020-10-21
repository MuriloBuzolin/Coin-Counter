import cv2
import numpy as np

img_inicial = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas1.jpeg')
mask_inv = cv2.bitwise_not(mask)


cv2.imshow('original', img_inicial)

cv2.waitKey(0)
cv2.destroyAllWindows