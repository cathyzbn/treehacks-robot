import os
import cv2 as cv
import numpy as np
from cvzone.HandTrackingModule import HandDetector


# Contains operations to perform on an individual frame
class FrameOperations():

    def __init__(self):
        self.face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.hand_detector = HandDetector(detectionCon=0.8)

    # Detects faces: 
    # - accepts frame as img
    # - returns img with bounding boxes
    def detect_faces(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Detect the faces
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
        return img

    # Detects hands:
    # - accepts frame image
    # - returns img with bounding boxes around hands (specific to 21 joints) 
    def detect_hands(self, frame):
        hands, img = self.hand_detector.findHands(frame)

        if hands:
            # Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points
            bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
            centerPoint1 = hand1['center']  # center of the hand cx,cy
            handType1 = hand1["type"]  # Handtype Left or Right
            # Hand 2
            if len(hands) > 1:
                hand2 = hands[1]
                lmList2 = hand2["lmList"]  # List of 21 Landmark points
                bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
                centerPoint2 = hand2['center']  # center of the hand cx,cy
                handType2 = hand2["type"]  # Handtype Left or Right
                hand_height = bbox2[3] if bbox2[3] < bbox1[3] else bbox1[3]
        return img
