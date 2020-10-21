import cv2
import numpy as np

img_inicial = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas1.jpeg')
img_cinza = cv2.cvtColor(img_inicial, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(img_inicial, 180, 210, cv2.THRESH_BINARY)
_, threshold1 = cv2.threshold(img_cinza, 180, 210, cv2.THRESH_BINARY)

cv2.imshow('original33', threshold)
cv2.imshow('original332', threshold1)
#cv2.imshow('original', img_inicial)




cv2.waitKey(0)
cv2.destroyAllWindows