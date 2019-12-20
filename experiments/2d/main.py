from organisms import Blob
from planets import Space
import random

space = Space(dimx=100, dimy=100)
for i in range(40,70,10):
    for j in range(40,70,10):
        space.create_blob(i, j, val=(1,1,1))

while True:
    for coord, blob in space.organisms.copy().items():
        blob.next(space)
    space.render()