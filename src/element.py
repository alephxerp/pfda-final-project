import pygame, os

class Element(pygame.sprite.Sprite):
    def __init__(self, position : tuple[int, int], sprite : str) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.position : tuple[int, int] = position

        self.image : pygame.Surface = pygame.image.load(os.path.join("assets", sprite)).convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect()
        self.rect.topleft = self.position

        self.size : tuple[int, int] = self.rect.size

        self.dead : bool = False


    def on_hover(self) -> None:
        print("Hovering.")

    
    def on_click(self) -> None:
        if self.dead:
            self.image = pygame.image.load(os.path.join("assets", "tree.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        
        self.dead = not self.dead
        print("I have been clicked!")


    def update(self) -> None:
        pass