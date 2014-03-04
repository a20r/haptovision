
class PrintEvent(object):

    def __init__(self):
        self.counter = 0


    def run(self, **kwargs):
        self.counter += 1
        print "=== Text Event === ::", self.counter
        for key, value in kwargs.iteritems():
            print key, "=", value
        print ""
