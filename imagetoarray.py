from PIL import Image
import numpy as np
import os.path
import cv2


trainingArray = open('trainedCharacterData88.txt','a')
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachPart in imageArray:
        for theParts in eachPart:
            avgNum = reduce(lambda x, y: x + y, theParts[:3]) / len(theParts[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                # eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                # eachPix[3] = 255
    return newAr

dim = (8,8)
counter = 1
for i in range(65,91):
    counter = 1
    path = 'C:\Users\Akshay\Desktop\Mini Project\Character Recognition\dataset'+"\\"+chr(i)
    
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            filename = os.path.join(path,file)
            
            #print(filename)
            image = cv2.imread(filename,0)
            image = cv2.medianBlur(image,5)
            resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
            ret, th1 = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            th2 = cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)

            rpath = 'C:\Users\Akshay\Desktop\Mini Project\Character Recognition\crop_dataset'+"\\"+chr(i)+'\img88-'+str(counter)+'.jpg'
            #cv2.imshow('window',th1)
            cv2.imwrite(rpath,th2)
            im = cv2.imread(rpath)
            arr = np.asarray(im)
            arr = threshold(arr)
            array_image = str(arr.tolist())
            lineToWrite = chr(i)+'::'+array_image+'\n'

            trainingArray.write(lineToWrite)
            counter +=1
            #print(arr)
            #cv2.waitKey(0)

