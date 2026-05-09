import pygame, os

class Element(pygame.sprite.Sprite):
    def __init__(self, sprite : str, position : tuple[int, int] = (0, 0)) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.position : tuple[int, int] = position

        self.image : pygame.Surface = pygame.image.load(os.path.join("assets", sprite)).convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect()
        self.rect.center = self.position

        self.size : tuple[int, int] = self.rect.size

        self.dead : bool = False


    def on_hover(self) -> None:
        newsize : tuple[int, int] = tuple(size + size // 10 for size in self.size)

        self.image = pygame.transform.scale(self.image, newsize)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    
    def on_click(self) -> None:
        if self.dead:
            self.image = pygame.image.load(os.path.join("assets", "tree.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        
        self.dead = not self.dead


    def update(self) -> None:
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


class ElementGroup(pygame.sprite.Group):
    def __init__(self, position : tuple[int, int] = (0, 0)) -> None:
        pygame.sprite.Group.__init__(self)

        self.image : pygame.Surface = pygame.Surface((1920, 1080))
        self.position : tuple[int, int] = position
    

    def create(self, sprite : str, position : tuple[int, int] = (0, 0)) -> Element:
        element : Element = Element(sprite, position)
        self.add(element)

        return element


    def process(self) -> None:
        for element in self:
            element.update()
    

    def render(self) -> pygame.Surface:
        self.image.fill((0, 0, 0))
        self.draw(self.image)

        return self.image

