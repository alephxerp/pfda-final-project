import pygame

class Mouse:
    position : tuple[int, int] = (0, 0)
    left_click = False
    right_click = False

    def update(self, viewport : pygame.Surface, screen : pygame.Surface) -> None:
        self.position = tuple(real * viewportsize / screensize for real, viewportsize, screensize in zip(pygame.mouse.get_pos(), viewport.size, screen.size))
        self.left_click = pygame.mouse.get_just_pressed()[0]
        self.right_click = pygame.mouse.get_just_pressed()[2]

