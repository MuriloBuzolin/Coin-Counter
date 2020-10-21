import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\MURILO\Desktop\Python2\Projeto_Cofrinho\Moedas3.jpeg',0)
img = cv2.medianBlur(img,5)
img = cv2.resize(img, (900,750))

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
'''
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
'''
circles = cv2.HoughCircles( th3, cv2.HOUGH_GRADIENT,1,80, param1=100, param2=30, minRadius=35,maxRadius=65)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),2)

cv2.imshow('img', img)
cv2.imshow('th3', th3)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()