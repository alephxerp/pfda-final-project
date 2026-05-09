import pygame, os

class Element(pygame.sprite.Sprite):
    def __init__(self, sprite : str, position : tuple[int, int] = (0, 0)) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.position : tuple[int, int] = position

        self.image : pygame.Surface = pygame.image.load(os.path.join("assets", sprite)).convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect()
        self.rect.topleft = self.position

        self.size : tuple[int, int] = self.rect.size

        self.dead : bool = False


    def on_hover(self) -> None:
        newsize : tuple[int, int] = tuple(size + size // 10 for size in self.size)

        self.image = pygame.transform.scale(self.image, newsize)
        self.rect = self.image.get_rect()

    
    def on_click(self) -> None:
        if self.dead:
            self.image = pygame.image.load(os.path.join("assets", "tree.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        
        self.dead = not self.dead


    def update(self) -> None:
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()


class ElementGroup(pygame.sprite.Group):
    def __init__(self, position : tuple[int, int] = (0, 0)):
        pygame.sprite.Group.__init__(self)