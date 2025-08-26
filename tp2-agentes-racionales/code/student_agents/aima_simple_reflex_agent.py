import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent


class AIMA_Agent(BaseAgent):
    def __init__(self, server_url="http://localhost:5000", **kwargs):
        super().__init__(server_url, "AIMA_Agent", **kwargs)
        self.size = None

    def get_strategy_description(self):
        return "La «geografía» del entorno se conoce a priori"

    def think(self):
        if not self.is_connected():
            return False

        perception = self.get_perception()
        if not perception or perception.get("is_finished", True):
            return False

        # Your logic here
        if perception.get("is_dirty", False):
            return self.suck()
        else:
            x, y = perception.get("position")

            if not self.size:
                state = self.get_environment_state()
                grid = state.get("grid")
                self.size = (len(grid[0]), len(grid))

            size_x, size_y = self.size

            return random.choice(
                [
                    getattr(self, direction)
                    for direction, condition in {
                        "up": y > 0,
                        "down": y < size_y - 1,
                        "left": x > 0,
                        "right": x < size_x - 1,
                    }.items()
                    if condition
                ]
            )()
