# import pygame
from typing import Any

# from game_data import levels


class Overworld:
    def __init__(self,
                 start_level: float,
                 max_level: float,
                 surface: Any) -> None:

        # setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

    def run(self) -> None:
        ...
