import pygame, os
from element import Element

class Button(Element):
    def __init__(self, sprite : str, function : callable, *args, position : tuple[int, int] = (0, 0)) -> None:
        Element.__init__(self, sprite, position)

        self.function : callable = function
        self.args : tuple = args

    
    def on_click(self):
        return self.function(*self.args)