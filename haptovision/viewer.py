
import sys
import cv2
import feedback as fb

class Viewer(object):

    def __init__(self, filename):
        self.filename = filename
        self.img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
        self.fc = fb.DerivativeFeedbackController(20)
        edge_event = fb.events.EdgeEvent(self.img)
        text_event = fb.events.TextEvent()
        self.fc += edge_event
        self.fc += text_event


    def on_mouse(self, event, x, y, flags, param):
        self.fc.push(self.img, x, y)


    def run(self):
        cv2.imshow(self.filename, self.img)
        cv2.setMouseCallback(self.filename, self.on_mouse)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

