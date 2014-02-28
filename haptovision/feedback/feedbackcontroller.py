
class FeedbackController(object):

    def __init__(self):
        self.event_list = list()


    def trigger(self, *args, **kwargs):
        for event in self.event_list:
            event.run(*args, **kwargs)


    def add_event(self, val):
        if hasattr(val, "run"):
            self.event_list.append(val)
