import os
import cv2 as cv
import numpy as np


# Contains operations to perform on an individual frame
class FrameOperations():

    def __init__(self):
        self.face_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        self.distance = None
        self.img_index = 0

    # Detects faces: 
    # - accepts frame as img
    # - returns img with bounding bodes
    def detect_faces(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Detect the faces
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            self.distance = 4500 / w
        return img

    def img_capture(self, frame):
        cv.imwrite(filename=f'imgs/{self.img_index}.jpg', img=frame)
        print(f"Image number {self.img_index} saved!")
        self.img_index = self.img_index + 1
