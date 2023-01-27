import cv2
import numpy as np


frameWidth = 640
frameHeight = 480


cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty():
    pass
