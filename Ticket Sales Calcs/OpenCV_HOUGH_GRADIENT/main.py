
#Python code to determine how many tickets are sold and unsold. 

#requires screenshot of the image with sold and unsold seats depicted as dots.
#This code uses the Hough Gradient algorithm from Open CV to detect and identify "circles" which rep seats in the stadium.

#the meduim blur algorthim can be updated as needed.




import cv2
import numpy as np


  //colab patch for bug
from google.colab.patches import cv2_imshow

bcount = 0

  image = cv2.imread('xxx')
# insert screenshot of venue map
blur = cv2.medianBlur(image, 4)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,100,255, cv2.THRESH_BINARY_INV)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

min_area = 2
black_dots = []
for c in cnts:
   area = cv2.contourArea(c)
   if area > min_area:
      cv2.drawContours(image, [c], -1, (36, 255, 12), 2)
      black_dots.append(c)

     print("Dark Dots Count is:",len(black_dots))
cv2_imshow( image)
cv2.waitKey()


     image = cv2.imread('xxxx')
# insert screenshot of venue map

blur = cv2.medianBlur(image, 5)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,300,300, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

min_area = 0.1
white_dots = []
for c in cnts:
   area = cv2.contourArea(c)
   if area > min_area:
      cv2.drawContours(image, [c], -1, (36, 255, 12), 2)
      white_dots.append(c)

     print("Greyed-out Dots count is:",len(white_dots))
cv2_imshow( image)
cv2.waitKey()


