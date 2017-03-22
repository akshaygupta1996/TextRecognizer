import numpy as np
import cv2



def getPrintOrder(filepath):

    graph = []
    graph_1 = []

    
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    _,thresh = cv2.threshold(gray,160,255,cv2.THRESH_BINARY_INV)  #THRESH_BINARY_INV  THRESH_BINARY
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 15)
    contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours
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

    return print_order
                

filepath= 'tempPic.jpg'

print_order = getPrintOrder(filepath)
print(print_order)

for coordinate in print_order:
    [x,y,w,h] = coordinate
    print(x)
    print(y)
    print(w)
    print(h)

        

