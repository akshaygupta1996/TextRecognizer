import cv2
import numpy as np
from PIL import Image
from collections import Counter
np.seterr(over='ignore')

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


def getPrintOrder(filepath):

    #print "In Get Print Order Function"

    graph = []
    graph_1 = []

    
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    _,thresh = cv2.threshold(gray,160,255,cv2.THRESH_BINARY_INV)  #THRESH_BINARY_INV  THRESH_BINARY
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 15)
    _, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours
    #print contours
    for contour in contours:
        d = dict()
        point = []
        [x,y,w,h] = cv2.boundingRect(contour)

        if h>150 or w>300:
            continue

        if h<40 or w<40:
            continue

        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
        #cv2.imwrite('cccc.jpg',image)
        #print x, y, x+w,y+h
        point.append(x)
        point.append(y)
        point.append(w)
        point.append(h)
        d['x'] = x
        d['y'] = y
        d['w'] = w
        d['h'] = h
        graph.append(d)
        graph_1.append(point)

    num = len(graph)
    #print num
    #print graph_1
    mean_h = 0
    mean_w = 0
    for item in graph:
        mean_h = mean_h + item['h']
        mean_w = mean_w + item['w']

    mean_h = mean_h/num
    mean_w = mean_w/num

    #print mean_h, mean_w


    sorted_coor = sorted(graph_1, key = lambda k: [k[1], k[0]])
    #print sorted_coor
    print_order = []
    prev_c = []
    new = []
    counter = 0
    l = 1
    for p in sorted_coor:

        if counter == 0:
                prev_c = p
                print_order.append(p)
                counter = counter + 1
        else:
            
            if p[1] - prev_c[1] <= mean_h:
    #            print "length is small" , (p[1] - prev_c[1])
                print_order.insert(l-1,p)
                prev_c = p
            else:
    #            print "length is big new line"
                print_order.append([-1,-1,-1,-1])
                print_order.append(p)
                l = len(print_order)
                new.append(l-2)
                prev_c = p

    #    print(print_order)
    #    print(new)

    prev = 0
    for n in new:
        print_order[prev:n]=sorted(print_order[prev:n],key = lambda k: k[0])
        prev = n
    #print print_order
    return print_order

def whatNumIsThis(iar):

    matchedAr = []
    loadExamps = open('C:\Users\Akshay\Desktop\Mini Project\CharacterRecognition\\trainedCharacterData88.txt','r').read()
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
                    #print(a)
                    #print(b)
                    matchedAr.append(str(currentNum))

                x+=1
        except Exception as e:
            print(str(e))
                
    x = Counter(matchedAr)
    ch.append(sorted(x,key=x.get)[-1])

    #print(x)


def getImage(filepath):
    #print "In get Image Function"
    co = 0
    image = cv2.imread(filepath)
##    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
##    _,thresh = cv2.threshold(gray,160,255,cv2.THRESH_BINARY_INV)  #THRESH_BINARY_INV  THRESH_BINARY
##    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
##    dilated = cv2.dilate(thresh,kernel,iterations = 15)
##    contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours

    print_order = getPrintOrder(filepath)
    #print "After Print Order Func"
    #print print_order
    for coordinate in print_order:
        [x,y,w,h] = coordinate
        if x == -1:
            ch.append('\n')
            continue
##    for contour in contours:
##        [x,y,w,h] = cv2.boundingRect(contour)
##
##        if h>150 or w>300:
##            continue
##
##        if h<40 or w<40:
##            continue
##
##        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
##        #cv2.imwrite('cccc.jpg',image)
##        print x, y, x+w,y+h
        cropped = image[y :y +  h , x : x + w]
        f = 'C:\Users\Akshay\Desktop\Mini Project\CharacterRecognition\crop_trim'+str(co)+'.jpg'
        cv2.imwrite(f, cropped)
        img = cv2.imread(f,0)
        img = cv2.medianBlur(img,5)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
        
        th2 = cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)

        rpath = 'C:\Users\Akshay\Desktop\Mini Project\CharacterRecognition\\test_crop\img.jpg'
        cv2.imwrite(rpath,th2)
        im = cv2.imread(rpath)
        arr = np.asarray(im)
        arr=threshold(arr)
        array_image = str(arr.tolist())
        #print(array_image)
        whatNumIsThis(arr)
        #print ch
        co = co + 1
        
    
    


dim = (8,8)
ch = []
filepath_p = 'tempPic.jpg'
getImage(filepath_p)
#for i in range(232, 253):
#        path = 'C:\Users\Akshay\Desktop\Mini Project\CharacterRecognition\\test\crop_'+str(i)+'.jpg'
#        
#        image = cv2.imread(path,0)
#        image = cv2.medianBlur(image,5)
#        resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
#        th2 = cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#                cv2.THRESH_BINARY,11,2)

#        rpath = 'C:\Users\Akshay\Desktop\Mini Project\CharacterRecognition\\test_crop\imgc-'+str(i)+'.jpg'
#        cv2.imwrite(rpath,th2)
#        im = cv2.imread(rpath)
#        arr = np.asarray(im)
#        arr=threshold(arr)
#        array_image = str(arr.tolist())
        #print(array_image)
#        whatNumIsThis(arr)
        #raw_input()
print(''.join(c for c in ch))






        
