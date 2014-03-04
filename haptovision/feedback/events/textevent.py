
class TextEvent(object):

    def run(self, **kwargs):
        print "=== Text Event ==="
        for key, value in kwargs.iteritems():
            print key, "=", value
        print ""
