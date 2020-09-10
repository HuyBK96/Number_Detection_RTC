from  process_image import get_output_image
import numpy as np
import cv2

x = 250
y = 180
w = 140
h = 140

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, img = cap.read()

    fname = "out.png"
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
    img_crop = img[y:y+h, x:x+w, :]
    gray_crop = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray_crop,127,255,cv2.THRESH_BINARY)
    #thresh = cv2.adaptiveThreshold(gray_crop,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imwrite(fname, thresh)
    get_output_image(fname)
    
    cv2.imshow('video',img)
    cv2.imshow('crop',thresh)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
