import cv2
import numpy as np


img = cv2.imread('hadtodoittoem.png')
sharp_filter = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]) #kernel can be changed any other matrix (e.g. blur, detect edges, etc.)
final = np.zeros(shape=(len(img),len(img[0]),3))

#iterates through every pixel, generates a temporary 3x3 matrix and applies the convolution
#if-else clauses necessary for extend-type padding
for c in range(3):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if (i == 0):
                if (j == 0):
                    temp = np.array([[img[0,0,c],img[0,0,c],img[0,1,c]],[img[0,0,c],img[0,0,c],img[0,1,c]],[img[1,0,c],img[1,0,c],img[1,1,c]]])
                elif (j == len(img[0])-1):
                    temp = np.array([[img[0,j-1,c],img[0,j,c],img[0,j,c]],
                    [img[0,j-1,c],img[0,j,c],img[0,j,c]],
                    [img[1,j-1,c],img[1,j,c],img[1,j,c]]])
                else:
                    temp = np.zeros(shape=(3,3))
                    for b in range(3):
                        temp[0,b] = img[0,j+b-1,c]
                    for a in range(1,3):
                        for b in range(3):
                            temp[a,b] = img[a-1,j+b-1,c]
            elif (i == len(img)-1):
                if (j == 0):
                    temp = np.array([[img[i-1,0,c],img[i-1,0,c],img[i-1,1,c]],[img[i,0,c],img[i,0,c],img[i,1,c]],[img[i,0,c],img[i,0,c],img[i,1,c]]])
                elif (j == len(img[0])-1):
                    temp = np.array([[img[i-1,j-1,c],img[i-1,j,c],img[i-1,j,c]],[img[i,j-1,c],img[i,j,c],img[i,j,c]],[img[i,j-1,c],img[i,j,c],img[i,j,c]]])
                else:
                    temp = np.zeros(shape=(3,3))
                    for a in range(len(img)-2,len(img)):
                        for b in range(3):
                            temp[a-len(img)+2,b] = img[a,j+b-1,c]
                    for b in range(3):
                        temp[2,b] = img[i,j+b-1,c]
            else:
                if (j == 0):
                    temp = np.zeros(shape=(3,3))
                    for a in range(3):
                        temp[a,0] = img[i+a-1,j,c]
                        for b in range(1,3):
                            temp[a,b] = img[i+a-1,j+b-1,c]
                elif (j == len(img[0])-1):
                    temp = np.zeros(shape=(3,3))
                    for a in range(3):
                        for b in range(1,2):
                            temp[a,b] = img[i+a-1,j+b-1,c]
                        temp[a,2] = img[i+a-1,j,c]
                else:
                    temp = np.zeros(shape=(3,3))
                    for a in range(3):
                        for b in range(3):
                            temp[a,b] = img[i+a-1,j+b-1,c]
            prod = temp*sharp_filter
            #needs to divide by 255 to achieve the right brightness by normalizing its level
            final[i,j,c]=np.sum(prod)/255 #additionally, divide by the number required by the desired filter (e.g. divide by 9 for average filter)
        
#press q to close images
while(True):
    cv2.imshow('original',img)
    cv2.imshow('final', final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
