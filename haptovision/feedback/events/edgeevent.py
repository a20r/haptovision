
import cv2
import numpy as np

class EdgeEvent(object):

    def __init__(self, img):
        self.img = np.zeros_like(img)
        self.disp_name = "Edge Drawing"
        cv2.imshow(self.disp_name, self.img)


    def run(self, **kwargs):
        x = kwargs.get("x", 0)
        y = kwargs.get("y", 0)
        diff = kwargs.get("diff", (255, 255, 255))
        print diff
        cv2.circle(self.img, (x, y), 4, diff, -1)
        cv2.imshow(self.disp_name, self.img)


