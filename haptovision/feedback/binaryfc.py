
import sys
import feedbackcontroller as fc

class BinaryFeedbackController(fc.FeedbackController):

    def __init__(self):
        self.already_inside_poly = False
        self.should_fire = False
        self.event_list = list()
        super(fc.FeedbackController, self).__init__()


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


    def push(self, poly_list, x, y):
        in_poly = any(
            [self.pointInPoly([x, y], poly.getConvexHull()) for poly in poly_list]
        )

        if in_poly and not self.already_inside_poly:
            self.already_inside_poly = True
            self.trigger(x, y)
            return True

        if not in_poly and self.already_inside_poly:
            self.already_inside_poly = False
            self.trigger(x, y)
            return True

        return False
