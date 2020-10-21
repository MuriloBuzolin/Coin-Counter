import cv2
import numpy as np
 
img_inicial = cv2.imread('C:\\Users\\MURILO\\Desktop\\Python2\\Projeto_Cofrinho\\Moedas1.jpeg')
img_cinza = cv2.cvtColor(img_inicial, cv2.COLOR_BGR2GRAY)
#img_antes = cv2.Canny(img_cinza, 200, 300, 5)
img_agr = cv2.Canny(img_cinza, 150, 400, 5)


#cv2.imshow('imagem', img_inicial)
#cv2.imshow('imagem1', img_cinza)
cv2.imshow('imagem_agr', img_agr)
#cv2.imshow('imagem_antes', img_antes)

cv2.waitKey(0)
cv2.destroyAllWindows