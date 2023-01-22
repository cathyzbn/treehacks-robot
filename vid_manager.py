import cv2 as cv
from frame_ops import FrameOperations

font                   = cv.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
thickness              = 1
lineType               = 2

class VideoManager():

    def __init__(self):
        self.FRAME_OPS = FrameOperations()
        self.font                   = cv.FONT_HERSHEY_SIMPLEX
        self.bottomLeftCornerOfText = (10,500)
        self.fontScale              = 1
        self.fontColor              = (255,255,255)
        self.thickness              = 1
        self.lineType               = 2

    # Infinite loop for video capture
    def get_vid(self, webcam_id):
        cap = cv.VideoCapture(webcam_id)

        try:
            # Infinite Play Loop
            while (True):
                has_frame, frame = cap.read()
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
                try:
                    # Facial detection
                    frame = self.FRAME_OPS.detect_faces(frame)
                    cv.putText(
                        frame, 
                        f'{self.FRAME_OPS.distance}',
                        self.bottomLeftCornerOfText, 
                        self.font, 
                        self.fontScale,
                        self.fontColor,
                        self.thickness,
                        self.lineType
                    )
                    cv.imshow('Video Output', frame)

                except Exception as e:
                    print('Exception: ', e)
                    break

        except KeyboardInterrupt:
            print('End Program.')