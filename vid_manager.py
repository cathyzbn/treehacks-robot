import cv2 as cv
from frame_ops import FrameOperations


class VideoManager():

    def __init__(self):
        self.FRAME_OPS = FrameOperations()

    def get_vid(self, webcam_id):

        cap = cv.VideoCapture(webcam_id)

        try:
            fps = 30

            # Infinite Play Loop
            while (True):
                has_frame, frame = cap.read()
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
                try:
                    # open cv code goes here
                    frame = self.FRAME_OPS.detect_faces(frame)
                    cv.imshow('Video Output', frame)
                except Exception as e:
                    print('Exception: ', e)
                    break

        except KeyboardInterrupt:
            print('End Program.')