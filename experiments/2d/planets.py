import numpy as np
import cv2
from organisms import Blob


class Space:
    def __init__(self, dimx, dimy, display=True):
        self.dimx = dimx
        self.dimy = dimy
        self.organisms = {}
        self.space = np.zeros(shape=(dimx, dimy, 3))
        self.display = display
        if self.display:
            cv2.namedWindow("Life", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Life", 600, 600)

    def create_blob(self, x, y, colour):
        blob = Blob(x, y, colour)
        self.organisms[(x, y)] = blob
        self.space[x, y] = blob.colour

    def delete_blob(self, x, y):
        del self.organisms[(x, y)]
        self.space[x, y] = (0, 0, 0)

    def render(self, speed=100):
        cv2.imshow("Life", self.space)
        cv2.waitKey(speed)
