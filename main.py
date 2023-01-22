from vid_manager import VideoManager
import os


class Main():

    def __init__(self):
        self.VI_M = VideoManager()

    def live_estimation(self, webcam_id=0):
        self.VI_M.get_vid(webcam_id)


if __name__ == "__main__":
    app = Main()
    app.live_estimation(webcam_id=0)
