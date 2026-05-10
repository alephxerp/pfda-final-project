import pygame, os

class Element(pygame.sprite.Sprite):
    def __init__(self, sprite : str, position : tuple[int, int] = (0, 0)) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.position : tuple[int, int] = position

        self.image : pygame.Surface = pygame.image.load(os.path.join("assets", sprite)).convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect()
        self.rect.center = self.position

        self.size : tuple[int, int] = self.rect.size


    def on_hover(self) -> None:
        newsize : tuple[int, int] = tuple(size + size // 10 for size in self.size)

        self.image = pygame.transform.scale(self.image, newsize)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    
    def on_click(self) -> None:
        pass


    def update(self) -> None:
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


class ElementGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        pygame.sprite.Group.__init__(self)

        self.background : pygame.Surface = pygame.Surface((1920, 1080))
        self.background.fill((0, 0, 0))
        self.image : pygame.Surface = self.background.copy()
    

    def create(self, sprite : str, position : tuple[int, int] = (0, 0)) -> Element:
        element : Element = Element(sprite, position)
        self.add(element)

        return element


    def process(self) -> None:
        for element in self:
            element.update()
    

    def set_background(self, background : pygame.Surface) -> pygame.Surface:
        self.background = background
        return self.background


    def render(self) -> pygame.Surface:
        self.image = self.background.copy()
        self.draw(self.image)

        return self.image

