import cv2
import numpy as np

def get_limit(color):

    c=np.uint8([[color]])
    hsvC=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lower_limit=hsvC[0][0][0] - 10,100,100   #to ignore very dark or grayish colors
    upper_limit=hsvC[0][0][0] + 10,255,255

    lower_limit=np.array(lower_limit,dtype=np.uint8)
    upper_limit=np.array(upper_limit,dtype=np.uint8)

    return lower_limit, upper_limit


print(get_limit([0,255,255]))

