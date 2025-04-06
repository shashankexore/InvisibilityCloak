import cv2
import numpy as np

def hello(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("bars")

cv2.createTrackbar("upper_hue", "bars", 110, 180, hello)
cv2.createTrackbar("upper_saturation", "bars", 255, 255, hello)
cv2.createTrackbar("upper_value", "bars", 255, 255, hello)
cv2.createTrackbar("lower_hue", "bars", 68, 180, hello)
cv2.createTrackbar("lower_saturation", "bars", 55, 255, hello)
cv2.createTrackbar("lower_value", "bars", 54, 255, hello)

while True:
    ret, init_frame = cap.read()
    if ret:
        break

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    inspect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    upper_hue = cv2.getTrackbarPos("upper_hue", "bars")
    upper_saturation = cv2.getTrackbarPos("upper_saturation", "bars")
    upper_value = cv2.getTrackbarPos("upper_value", "bars")
    lower_hue = cv2.getTrackbarPos("lower_hue", "bars")
    lower_saturation = cv2.getTrackbarPos("lower_saturation", "bars")
    lower_value = cv2.getTrackbarPos("lower_value", "bars")
    
    kernel = np.ones((3, 3), np.uint8)
    
    upper_hsv = np.array([upper_hue, upper_saturation, upper_value])
    lower_hsv = np.array([lower_hue, lower_saturation, lower_value])
    
    mask = cv2.inRange(inspect, lower_hsv, upper_hsv)
    mask = cv2.medianBlur(mask, 3)
    mask_inv = 255 - mask
    mask = cv2.dilate(mask, kernel, iterations=5)
    
    b, g, r = cv2.split(frame)
    b = cv2.bitwise_and(mask_inv, b)
    g = cv2.bitwise_and(mask_inv, g)
    r = cv2.bitwise_and(mask_inv, r)
    frame_inv = cv2.merge((b, g, r))
    
    b, g, r = cv2.split(init_frame)
    b = cv2.bitwise_and(b, mask)
    g = cv2.bitwise_and(g, mask)
    r = cv2.bitwise_and(r, mask)
    blanket_area = cv2.merge((b, g, r))
    
    final = cv2.bitwise_or(frame_inv, blanket_area)
    
    cv2.imshow("invisible", final)
    cv2.imshow("original", frame)
    
    if cv2.waitKey(3) == ord('x'):
        break

cv2.destroyAllWindows()
cap.release()
