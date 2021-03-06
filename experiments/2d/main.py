from organisms import Blob
from planets import Space
import random

space = Space(dimx=200, dimy=200)
for i in range(80,120,10):
    for j in range(80,120,10):
        space.create_blob(i, j, colour=(1,1,1))

while True:
    for coord, blob in space.organisms.copy().items():
        blob.next(space)
    space.render()