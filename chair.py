import cv2
import pickle
import cvzone
import numpy as np

# Video feed
cap = cv2.VideoCapture('test.mp4')

while True:

    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    cv2.imshow("Image", img)
    cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageThres", imgMedian)
    cv2.waitKey(10)