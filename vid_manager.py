import cv2 as cv
from frame_ops import FrameOperations

def key_equal(key, key_char):
    return key & 0xFF == ord(key_char)
class VideoManager():

    def __init__(self):
        self.FRAME_OPS = FrameOperations()

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
                cv.imshow('Video Output', frame_with_face)

                if key_equal(key, 'q'):
                    self.video_off(cap)
                    break
                elif key_equal(key, 's'):
                    self.FRAME_OPS.img_capture(frame_with_face)

            except KeyboardInterrupt:
                self.video_off()


