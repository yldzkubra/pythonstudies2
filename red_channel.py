import cv2 as cv
import numpy as np
import utm
import math

imge= cv.imread("/home/kubra/Downloads/redchannel.jpeg")
imgeHsv=cv.cvtColor(imge,cv.COLOR_BGR2HSV)

lower_red=np.array([160,50,50])
upper_red=np.array([180,255,255])
red_mask=cv.inRange(imgeHsv,lower_red,upper_red)
red=cv.bitwise_and(imge,imge,mask=red_mask)
cv.imshow("resim",red_mask)
cv.waitKey(0)
cv.imshow("resim",red)
cv.waitKey(0)

n2,contours,hiyerarsi = cv.findContours(red_mask,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

for i in contours:
	M = cv.moments(i)
	if M['m00'] != 0:
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])

x,y,zone,ut=utm.from_latlon(40.996207,29.060491)
newx=cx*0.0102645833
newy=cy*0.0102645833

lat_lon=utm.to_latlon(newx+x, newy+y, zone, ut)
print(x,y,zone,ut)
print(lat_lon)


