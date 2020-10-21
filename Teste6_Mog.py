import cv2
import numpy as np

img_inicial = cv2.imread('C:\\Users\\MURILO\\Desktop\\Python2\\Projeto_Cofrinho\\Moedas1.jpeg')
#img_cinza = cv2.cvtColor(img_inicial, cv2.COLOR_BGR2GRAY)
img_mod = cv2.createBackgroundSubtractorMOG2()

mascara_frente = img_mod.apply(img_inicial)

cv2.imshow('imagem0', img_inicial)
cv2.imshow('imagem1', mascara_frente)


cv2.waitKey()
cv2.destroyAllWindows()