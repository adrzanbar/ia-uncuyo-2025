import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent
from collections import deque


class AIMA_Agent(BaseAgent):

    directions = {"up": (0, -1), "left": (-1, 0), "down": (0, 1), "right": (1, 0)}

    def __init__(self, server_url="http://localhost:5000", **kwargs):
        super().__init__(server_url, "AIMA_Agent", **kwargs)
        self.size = None
        self.visited = set()

    def search(self, x, y):
        # BFS
        queue = deque([(x, y)])
        visited = set()
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in self.directions.values():
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in visited:
                    if (nx, ny) not in self.visited: return (nx, ny)

                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return None

    def think(self):
        if not self.is_connected():
            return False

        perception = self.get_perception()
        if not perception or perception.get("is_finished", True):
            return False

        x, y = perception.get("position")
        self.visited.add((x, y))

        if not self.size:
            env = self.get_environment_state()
            grid = env.get("grid")
            self.size = len(grid[0])

        if perception.get("is_dirty", False):
            return self.suck()

        for move, (dx, dy) in self.directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in self.visited:
                self.target = None
                return getattr(self, move)()
            
        if (x, y) == self.target:
            self.target = None

        self.target = self.search(x, y)
        if not self.target: return False

        tx, ty = self.target
        if ty < y:
            return self.up()
        elif tx < x:
            return self.left()
        elif ty > y:
            return self.down()
        elif tx > x:
            return self.right()
