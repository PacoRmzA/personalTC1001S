import cv2
import numpy as np


img = cv2.imread('doge.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #I don't know how to process an image with RGB channels
sharp_filter = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]) #kernel can be changed any other matrix (e.g. blur, detect edges, etc.)
final = np.zeros(shape=(len(gray),len(gray[0])))

#iterates through every pixel, generates a temporary 3x3 matrix and applies the convolution
for i in range(len(gray)):
    for j in range(len(gray[i])):
        if (i == 0):
            if (j == 0):
                temp = np.array([[gray[0,0],gray[0,0],gray[0,1]],[gray[0,0],gray[0,0],gray[0,1]],[gray[1,0],gray[1,0],gray[1,1]]])
            elif (j == len(gray)-1):
                temp = np.array([[gray[0,j-1],gray[0,j],gray[0,j]],
                [gray[0,j-1],gray[0,j],gray[0,j]],
                [gray[1,j-1],gray[1,j],gray[1,j]]])
            else:
                temp = np.zeros(shape=(3,3))
                for b in range(3):
                    temp[0,b] = gray[0,j+b-1]
                for a in range(1,3):
                    for b in range(3):
                        temp[a,b] = gray[a-1,j+b-1]
        elif (i == len(gray)-1):
            if (j == 0):
                temp = np.array([[gray[i-1,0],gray[i-1,0],gray[i-1,1]],[gray[i,0],gray[i,0],gray[i,1]],[gray[i,0],gray[i,0],gray[i,1]]])
            elif (j == len(gray)-1):
                temp = np.array([[gray[i-1,j-1],gray[i-1,j],gray[i-1,j]],[gray[i,j-1],gray[i,j],gray[i,j]],[gray[i,j-1],gray[i,j],gray[i,j]]])
            else:
                temp = np.zeros(shape=(3,3))
                for a in range(len(gray)-2,len(gray)):
                    for b in range(3):
                        temp[a-len(gray)+2,b] = gray[a,j+b-1]
                for b in range(3):
                    temp[2,b] = gray[i,j+b-1]
        else:
            if (j == 0):
                temp = np.zeros(shape=(3,3))
                for a in range(3):
                    temp[a,0] = gray[i+a-1,j]
                    for b in range(1,3):
                        temp[a,b] = gray[i+a-1,j+b-1]
            elif (j == len(gray)-1):
                temp = np.zeros(shape=(3,3))
                for a in range(3):
                    for b in range(1,2):
                        temp[a,b] = gray[i+a-1,j+b-1]
                    temp[a,2] = gray[i+a-1,j]
            else:
                temp = np.zeros(shape=(3,3))
                for a in range(3):
                    for b in range(3):
                        temp[a,b] = gray[i+a-1,j+b-1]
        prod = temp*sharp_filter
        #needs to divide by 254.5 to achieve the right brightness
        final[i,j]=np.sum(prod)/254.5 #additionally, divide by the number required by the desired filter (e.g. divide by 9 for average filter)
        
#press q to close images
while(True):
    cv2.imshow('original',gray)
    cv2.imshow('final', final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
