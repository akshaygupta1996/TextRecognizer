import cv2
import numpy as np
from PIL import Image

dim = (8,8)
i = 232
filename = 'C:\Users\Akshay\Desktop\Mini Project\CharacterRecognition\dataset\A\crop_0.jpg'

image = cv2.imread(filename,0)
image = cv2.medianBlur(image,5)
resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
th2 = cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)

cv2.imwrite('cropt_1.jpg',th2)
i= cv2.imread('cropt_1.jpg')

arr = np.asarray(i)
print(arr)
cv2.imshow('window',th2)
cv2.waitKey(0)
