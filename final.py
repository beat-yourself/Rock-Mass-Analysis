import cv2
import numpy as np
import math

img = cv2.read("image.jpg")  # take image as input
gray = cv2.cvtColor(img,COLOR_BGR2GRAY) # Convert image to grayscale


edges = cv2.Canny(gray,50,150, apertureSize = 3) #Apply Canny edge detector method on the grayscale image
lines = cv2.HoughLines(edges,1,np.pi/180,200)


print("Dip of the lines in the image")
sum=0
for i in range(0,len(lines)):
    for rho,thetha in lines[i]:
        sum+= np.pi/2- thetha
        print(np.pi/2-thetha)

print("Average value of dip is:" sum/len(lines))

num = len(lines)
x,y,dim = img.shape
dip = sum/num # average dip value in radian
m = num/(num+1)
'''
****Persistence length****
Persistence of discontinuities is one of the most
important rock mass parameters because it
defines, together with spacing, the size of blocks
that can slide from the face
'''

h = x*y/(x*math.cos(dip)+ y*math.sin(dip)) 
per_len = h*(1+m)/(1-m)
print("Persistence length  = ", per_len)


'''
****Spacing of discontinuities****
The spacing of discontinuities will determine the
dimensions of blocks in the slope, which will
influence the size of rock falls and the design of
bolting patterns.
'''

sp = s*math.sin(dip)
N = N_app/math.sin(dip)
print("Number of discontinuties", N)

# NJ = number of joints
# L1 = length o scan line

print("Average Spacing is",L1*math.cos(dip)/NJ)

    
