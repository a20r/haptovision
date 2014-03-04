
class FeedbackController(object):

    def __init__(self):
        self.event_list = list()


    def trigger(self, **kwargs):
        for event in self.event_list:
            event.run(**kwargs)


    def add_event(self, val):
        if hasattr(val, "run"):
            self.event_list.append(val)
