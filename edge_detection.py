import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret , frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5) 
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    can = cv2.Canny(frame, 200, 100)
    cv2.imshow('original', frame)
    #cv2.imshow('Sobelx', sobelx)
    #cv2.imshow('Sobely', sobely)
    cv2.imshow('Canny', can)
    #cv2.imshow('laplacian', laplacian)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
cap.release()