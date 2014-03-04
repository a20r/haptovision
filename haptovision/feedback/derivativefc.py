
import feedbackcontroller as fc
import math

class DerivativeFeedbackController(fc.FeedbackController):

    def __init__(self, min_color_diff):
        self.event_list = list()
        self.min_color_diff = min_color_diff
        self.prev_color = None
        super(fc.FeedbackController, self).__init__()


    def color_distance(self, c1, c2):
        c1 = map(int, c1)
        c2 = map(int, c2)

        return math.sqrt(
            pow(c1[0] - c2[0], 2) +
            pow(c1[1] - c2[1], 2) +
            pow(c1[2] - c2[2], 2)
        )


    def color_difference(self, c1, c2):
        c1 = map(int, c1)
        c2 = map(int, c2)

        return (
            abs(c1[0] - c2[0]),
            abs(c1[1] - c2[1]),
            abs(c1[2] - c2[2])
        )

    def push(self, img, x, y):
        if not self.prev_color is None:
            current_color = img[y, x]
            c_dist = self.color_distance(current_color, self.prev_color)
            if c_dist > self.min_color_diff:
                print c_dist
                c_diff = self.color_difference(self.prev_color, current_color)
                self.trigger(x=x, y=y, diff=c_diff)

        self.prev_color = img[y, x]

