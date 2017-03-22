import cv2
import numpy as np
from PIL import Image
from collections import Counter

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachPart in imageArray:
        for theParts in eachPart:
            # for the reduce(lambda x, y: x + y, theParts[:3]) / len(theParts[:3])
            # in Python 3, just use: from statistics import mean
            # then do avgNum = mean(theParts[:3])
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

    #print(newAr)
    return newAr

def whatNumIsThis(iar):

    matchedAr = []
    loadExamps = open('numArEx2.txt','r').read()
    loadExamps = loadExamps.split('\n')
    #i = Image.open(filePath)
    #iar = np.array(i)
    #iar = threshold(iar)
    iarl = iar.tolist()
    #print(iarl)
    inQuestion = str(iarl)
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            x = 0
            while x < len(eachPixEx):
                sa =eachPixEx[x].split(', ')
                # print sa
                a = ', '.join(sa[0:3])
                #print(a)
                b = eachPixInQ[x]
                if eachPixInQ[x][-1] == ']':
                    b = eachPixInQ[x][0:-1]
                #print(b)
                # raw_input()
                if a==b:
                    matchedAr.append(int(currentNum))

                x+=1
        except Exception as e:
            print(str(e))
                
    x = Counter(matchedAr)
    print(sorted(x,key=x.get)[-1])
    #print(x)

def getImage(filepath):
    
    image = cv2.imread(filepath,0)
    dim = (8,8)
    image = cv2.medianBlur(image,5)
    ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)

    resized = cv2.resize(th2,dim,interpolation = cv2.INTER_AREA)
    #cv2.imshow("resized",resized)
    #cv2.waitKey(0)
    cv2.imwrite("crop.jpg",resized)
    i = cv2.imread('crop.jpg')
    iar = np.array(i)
    #print(iar)
    iar = threshold(iar)
    #print(iar)


    #path = 'crop_6_trim.jpg'
    whatNumIsThis(iar)


dim=(16,16)
file_name='tempPic.jpg'
image = cv2.imread(file_name)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
_,thresh = cv2.threshold(gray,160,255,cv2.THRESH_BINARY_INV)  #THRESH_BINARY_INV  THRESH_BINARY
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 15)
contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours

index=231
for contour in contours:
    [x,y,w,h] = cv2.boundingRect(contour)

    if h>300 and w>100:
        continue

    if h<40 or w<40:
        continue

    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
    cropped = image[y :y +  h , x : x + w]
    #filepath = 'crop_trim.jpg'
    #cv2.imwrite(filepath, cropped)
    #getImage(filepath)

    s = 'test/crop_' + str(index) + '.jpg' 
    cv2.imwrite(s , cropped)
    #image = cv2.imread(s,0)
    #image = cropped
    #image = cv2.medianBlur(image,5)
    #resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
    #ret, th1 = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
    #th2 = cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    #    cv2.THRESH_BINARY,11,2)
    #cv2.imwrite(s,th2)
    #im = cv2.imread(rpath)
    
    index = index + 1

 
cv2.imwrite("testimages.jpg", image)
