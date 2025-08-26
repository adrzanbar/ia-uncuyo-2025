import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent


class SimpleReflexAgent(BaseAgent):
    directions = {"up": (0, -1), "left": (-1, 0), "down": (0, 1), "right": (1, 0)}

    def __init__(self, server_url="http://localhost:5000", **kwargs):
        super().__init__(server_url, "SimpleReflexAgent", **kwargs)

    def get_strategy_description(self):
        return """Select actions on the basis of the current percept, 
        ignoring the rest of the percept history. 
        Suck if dirty, otherwise move in a random direction."""

    def think(self):
        if not self.is_connected():
            return False

        perception = self.get_perception()
        if not perception or perception.get("is_finished", True):
            return False

        # Your logic here
        if perception.get("is_dirty", False):
            return self.suck()

        x, y = perception.get("position")

        return random.choice(
            [
                getattr(self, direction)
                for direction, (dx, dy) in self.directions.items()
                if x + dx >= 0 and y + dy >= 0
            ]
        )()
