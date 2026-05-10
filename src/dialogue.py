import pygame, os
from element import Element

class DialogueManager(Element):
    def __init__(self) -> None:
        Element.__init__(self, "dialogue_box.png")

        self.background : pygame.Surface = pygame.image.load(os.path.join("assets", "dialogue_box.png")).convert_alpha()
        self.image : pygame.Surface = self.background.copy()
        self.font : pygame.Font = pygame.font.SysFont("arial", 64)

        self.dialogue : list[str] = []
        self.index : int = 0

        self.rect : pygame.Rect = self.image.get_rect()
        self.rect.center = (960, 830)

        self.speaking : bool = False
    

    def on_hover(self) -> None:
        pass

    
    def on_click(self) -> None:
        if self.index >= len(self.dialogue):
            self.image = self.background.copy()
            self.speaking = False
        else:
            self.image = self.background.copy()
            self.speak()

    
    def start(self, dialogue : list[str]) -> None:
        self.dialogue = dialogue
        self.index = 0
        self.speaking = True

        self.speak()
    
    
    def speak(self) -> None:
        text : pygame.Surface = self.font.render(self.dialogue[self.index], True, (0, 0, 0))
        self.image.blit(text, (100, 100))
        
        self.index += 1
    

    def update(self) -> None:
        if not self.speaking:
            self.image = self.background.copy()

