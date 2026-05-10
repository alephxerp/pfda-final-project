import pygame, os
from element import Element, ElementGroup

class Character(Element):
    def __init__(self, sprite : str, dialogue : str, position : tuple[int, int] = (0, 0)) -> None:
        Element.__init__(self, sprite, position)

        self.dialogue : str = dialogue


    def on_click(self) -> str:
        return self.dialogue


class CharacterGroup(ElementGroup):
    def __init__(self) -> None:
        ElementGroup.__init__(self)
    

    def create(self, sprite : str, dialogue: str, position : tuple[int, int] = (0, 0)) -> Element:
        element : Character = Character(sprite, dialogue, position)
        self.add(element)

        return element

