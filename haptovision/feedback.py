
import sys
import pygame
import time

class FeedbackController(object):

    def __init__(self):
        self.event_list = list()


    def trigger(self):
        for event in self.event_list:
            event.run()


    def add_event(self, val):
        if hasattr(val, "run"):
            self.event_list.append(val)


class MouseFeedbackController(FeedbackController):

    def __init__(self):
        self.already_inside_poly = False
        self.should_fire = False
        self.event_list = list()
        super(FeedbackController, self).__init__()


    def rayintersectseg(self, p, edge):

        _eps = 0.00001
        _huge = sys.float_info.max
        _tiny = sys.float_info.min
        a, b = edge
        if a[1] > b[1]:
            a, b = b, a
        if p[1] == a[1] or p[1] == b[1]:
            p = (p[0], p[1] + _eps)

        intersect = False

        if (p[1] > b[1] or p[1] < a[1]) or (p[0] > max(a[0], b[0])):
            return False

        if p[0] < min(a[0], b[0]):
            intersect = True
        else:
            if abs(a[0] - b[0]) > _tiny:
                m_red = (b[1] - a[1]) / float(b[0] - a[0])
            else:
                m_red = _huge
            if abs(a[0] - p[0]) > _tiny:
                m_blue = (p[1] - a[1]) / float(p[0] - a[0])
            else:
                m_blue = _huge
            intersect = m_blue >= m_red
        return intersect


    def odd(self, x):

        return x % 2 == 1


    def pointInPoly(self, p, nodes):

        vecList = [[nodes[0][0], nodes[-1][0]]]
        for k in range(len(nodes) - 1):
            vecList += [[nodes[k][0], nodes[k + 1][0]]]

        return self.odd(
            sum(self.rayintersectseg(p, edge) for edge in vecList)
        )


    def should_trigger(self):
        return self.should_fire


    def push(self, poly_list, x, y):
        for poly in poly_list:
            in_poly = self.pointInPoly([x, y], poly.getConvexHull())
            if in_poly and not self.already_inside_poly:
                self.already_inside_poly = True
                self.trigger()

            if not in_poly and self.already_inside_poly:
                self.already_inside_poly = False
                self.trigger()


class SoundEvent(object):


    def __init__(self):
        pygame.init()


    def run(self):
        pygame.mixer.music.load("sounds/beep.wav")
        pygame.mixer.music.play()


def getSoundFeedbackController():

    mouse_feedback = MouseFeedbackController()
    sound_event = SoundEvent()
    mouse_feedback.add_event(sound_event)
    return mouse_feedback

