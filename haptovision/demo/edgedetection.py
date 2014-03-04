
import cv2
import sys

def compute_laplacian(img_file):

    img = cv2.imread(img_file, cv2.CV_LOAD_IMAGE_COLOR)
    img_lap = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    cv2.imshow("Laplacian", img_lap)


if __name__ == "__main__":
    compute_laplacian(sys.argv[1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

