import cv2 as cv
from frame_ops import FrameOperations

font                   = cv.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
thickness              = 1
lineType               = 2

def key_equal(key, key_char):
    return key & 0xFF == ord(key_char)
    
class VideoManager():

    def __init__(self):
        self.FRAME_OPS = FrameOperations()
        self.font                   = cv.FONT_HERSHEY_SIMPLEX
        self.bottomLeftCornerOfText = (10,500)
        self.fontScale              = 1
        self.fontColor              = (255,255,255)
        self.thickness              = 1
        self.lineType               = 2

    def video_off(self, cap):
        print("Turning off camera.")
        cap.release()
        print("Program ended.")
        cv.destroyAllWindows()
    
    def video_wait(self, ticks=1600):
        cv.waitKey(1650)

    # Infinite loop for video capture
    def get_vid(self, webcam_id, detect_face=True):
        cap = cv.VideoCapture(webcam_id)

        while (True):
            try:
            # Infinite Play Loop
                has_frame, frame = cap.read()
                key = cv.waitKey(1)
                if (detect_face):
                    frame_with_face = self.FRAME_OPS.detect_faces(frame)
                    cv.putText(
                        frame_with_face, 
                        f'{self.FRAME_OPS.distance}',
                        self.bottomLeftCornerOfText, 
                        self.font, 
                        self.fontScale,
                        self.fontColor,
                        self.thickness,
                        self.lineType
                    )
                cv.imshow('Video Output', frame_with_face)

                if key_equal(key, 'q'): # quit program
                    self.video_off(cap)
                    break 
                elif key_equal(key, 's'): # take a picture
                    self.FRAME_OPS.img_capture(frame_with_face) # TODO: change this to frame
                    self.video_wait()

            except KeyboardInterrupt:
                self.video_off()


