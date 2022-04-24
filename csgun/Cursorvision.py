
import cv2 
import time as t
import numpy as np
from pynput.mouse import Button, Controller
mouse = Controller()
capture = cv2.VideoCapture(2)
prev_frame_time = 0
new_frame_time = 0


# use this for Xserv: xhost local:root
# run script as superuser

while True:
    new_frame_time = t.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    gunX = 0
    gunY = 0
    _, frame = capture.read()
    erode = cv2.erode(frame, (5,5), 0)
    blur = cv2.GaussianBlur(erode, (5,5), 0)
    flipped = cv2.flip(blur, 1)
    cv2.putText(flipped, str(int(fps)), (20,50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255),2)

    hsv = cv2.cvtColor(flipped, cv2.COLOR_BGR2HSV)
    Lgreen = np.array([60, 20, 70])
    Hgreen = np.array([83 , 255,255])
    mask = cv2.inRange(hsv, Lgreen, Hgreen)

    contours,hierachy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    #cv2.drawContours(flipped, contours, -1, (255,0,0), 3)
    for i in range(0,len(contours),1):
        cnt = contours[i]

        if (cv2.contourArea(cnt) > 300):
            x,y,w,h = cv2.boundingRect(cnt)
            
            cv2.rectangle(flipped,(x,y),(x+w,y+h),(255,0,0),2)
            gunX = x
            gunY = y

    mouse.position = ( (gunX) * 3 , (gunY) * 3)

    #print(gunX, gunY)

    cv2.imshow("scan", flipped)
    cv2.imshow("output", mask)

    if cv2.waitKey(10) & 0xff == ord('p'):
        print("delete")
        break


    
         

# while True:
#     if __name__ == '__main__':
#         Thread(target = key).start()
#         Thread(target = vis).start()
#     if cv2.waitKey(10) & 0xff == ord('p'):
#         print("delete")
#         break
        
            
# def timer():  
#    shotTimer = False
#    sleep(0.1)
#    shotTimer = True


  
# Collect all event until released
# with Listener(on_press = show) as listener:
#     listener.join()

