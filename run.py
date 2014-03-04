
import haptovision as hv
import sys

def run(filename):
    viewer = hv.Viewer(filename)
    viewer.run()


def usage():
    return "Usage: python run.py [filename]"


if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print usage()

