import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Game:
    def __init__(self, size=(100, 100)):
        self.x, self.y = size
        self.board = np.zeros(shape=size)
        self.live = True
    def count(self):
        board = np.zeros((self.y+2,self.x+2))
        board[1:self.y+1, 1:self.x+1] = self.board.copy()

        counts = np.zeros((self.y, self.x))
        for y in range(1, self.y):
            for x in range(1, self.x):
                counts[y - 1, x - 1] = np.sum(board[y-1:y+2, x-1:x+2])\
                                       - board[y, x]
        self.live = int(np.sum(counts))
        return counts
    def update(self):
        counts = self.count()
        for y in range(self.y):
            for x in range(self.x):
                if self.board[y,x] == 1:
                    if counts[y,x] > 3:
                        self.board[y,x] = 0
                    elif counts[y,x] == 2 or counts[y,x] == 3:
                        self.board[y,x] = 1
                    elif counts[y,x] < 2:
                        self.board[y,x] = 0
                else:
                    if counts[y,x] == 3:
                        self.board[y,x] = 1
    def render(self, frames=100, speed=200):
        fig = plt.figure()
        def update(frame):
            self.update()
            return plt.imshow(self.board)
        ani = animation.FuncAnimation(fig, update, interval=speed)
        plt.show()

    def record(self, frames=100, speed=200):
        """Records. Does not render."""
        fig = plt.figure()
        vid = []
        f = 0
        while self.live and f <= frames:
            v = plt.imshow(self.board)
            vid.append([v])
            self.update()
            f += 1
        ani = animation.ArtistAnimation(fig, vid, interval=speed)
        ani.save("replays/0.mp4")

class Cell:
    def __init__(self, x, y):
        self.position = (x, y)
        self.neighbors = 0