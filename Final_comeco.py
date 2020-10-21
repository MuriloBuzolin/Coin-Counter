import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas3.jpeg', 0)

img = cv2.medianBlur(img,5)
#img = cv2.resize(img, (1280,928))   #entra com 1280p 928p

print(img.shape)


th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)


circles = cv2.HoughCircles( th3, cv2.HOUGH_GRADIENT,1,80, param1=100, param2=30, minRadius=35,maxRadius=65)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)#contorno
                    #Centro    raio
    
    #cv2.circle(img,(i[0],i[1]),2,(0,0,255),2)#centro
    break



img = cv2.resize(img, (900,750))
th3 = cv2.resize(th3, (900,750))

cv2.imshow('img', img)
cv2.imshow('th3', th3)
        

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
