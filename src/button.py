import pygame, os
from element import Element

class Button(Element):
    def __init__(self, sprite : str, function : callable, *args, position : tuple[int, int] = (0, 0)) -> None:
        Element.__init__(self, sprite, position)

        self.function : callable = function
        self.args : tuple = args

        self.rect.topleft = self.position

    
    def on_hover(self) -> None:
        Element.on_hover(self)
        self.rect.topleft = self.position


    def update(self) -> None:
        Element.update(self)
        self.rect.topleft = self.position


    def on_click(self):
        try:
            return self.function(*self.args)
        except Exception as e:
            print(f"{Exception} encountered while calling {self.function} on {self.args}")