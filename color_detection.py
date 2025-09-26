import cv2
from color_limit import  get_limit
from  PIL import  Image
 

def color_detectioon(color):
    cap=cv2.VideoCapture(0)

    while True:
        ret,frame=cap.read()

        hsvimage=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)

        lower_limit,upper_limit=get_limit(color=color)

        mask=cv2.inRange(hsvimage,lower_limit,upper_limit)

        mask_=Image.fromarray(mask)

        bbox=mask_.getbbox()

        if bbox is not None:
            x1,y1,x2,y2 =bbox

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
        print(bbox)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()

    cv2.destroyWindow()

