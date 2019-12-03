import numpy as np
import cv2

class Agent:
    def __init__(self, coord):
        self.x, self.y = coord

class Game:
    def __init__(self, size=(100, 100)):
        self.size = size
        self.x, self.y = self.size
        self.board = np.zeros(shape=size)
        self.agents = []
        self.live = False
    def add_agent(self, agent):
        assert type(agent) == Agentgi
        self.agents.append(agent)
        self.live = True
        self.update_board()
    def update_agents(self, new_agents):
        """Update agents (after a time step)"""
        self.agents = new_agents
        if len(self.agents) > 0:
            self.live = True
    def is_alive(self, alive, neighbors):
        """
        If alive, live if 2 <= neighbors <= 3
        If dead, live if neighbors == 3
        """
        if alive:
            return (neighbors==2 or neighbors==3)
        else:
            return (neighbors==3)
    def step(self):
        """Update alive agents"""
        board = np.zeros((self.y + 2, self.x + 2))
        board[1:self.y + 1, 1:self.x + 1] = self.board.copy()
        for agent in self.agents:
            x, y = agent.x, agent.y

        counts = np.negative(np.ones((self.y, self.x)))
        new_agents = []  # List of coordinates of new agents
        # For all agents, update neighbors
        for agent in self.agents:
            x, y = agent.x, agent.y
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    # Update if not already updated
                    if counts[j, i] == -1:
                        cnt = np.sum(board[j:j+3, i:i+3]) \
                                           - board[j+1, i+1]
                        counts[j, i] = cnt
                        if self.is_alive(board[j+1,i+1], cnt):
                            # print(i-1, j-1, board[j,i], cnt)
                            new_agents.append(Agent((i, j)))

        self.update_agents(new_agents)
        self.update_board()
    def update_board(self):
        self.board = np.zeros(shape=self.size)
        for agent in self.agents:
            x, y = agent.x, agent.y
            self.board[y, x] = 1
    def render(self, speed=10, frames=(600,600)):
        cv2.namedWindow("Life", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Life", frames[0], frames[1])
        while self.live:
            self.step()
            cv2.imshow("Life", self.board)
            cv2.waitKey(speed)
