import pygame, os
from element import Element

class DialogueManager(Element):
    def __init__(self) -> None:
        Element.__init__(self, "dialogue_box.png")

        self.background : pygame.Surface = pygame.image.load(os.path.join("assets", "dialogue_box.png")).convert_alpha()
        self.image : pygame.Surface = self.background.copy()
        self.font : pygame.Font = pygame.font.SysFont("arial", 64)

        self.rect : pygame.Rect = self.image.get_rect()
        self.rect.center = (960, 830)

        self.speaking : bool = False
    

    def on_hover(self) -> None:
        pass

    
    def on_click(self) -> None:
        if self.speaking:
            self.speaking = False
    
    
    def speak(self, dialogue : str) -> None:
        text : pygame.Surface = self.font.render(dialogue, True, (0, 0, 0))
        self.image.blit(text, (100, 100))
        self.speaking = True
    

    def update(self) -> None:
        if not self.speaking:
            self.image = self.background.copy()

