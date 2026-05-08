import pygame, sys


class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.position : tuple[int, int] = (0, 0)
        self.rect : pygame.Rect = pygame.Rect()
        self.image : pygame.Surface = pygame.image.load().convert_alpha()




def main():
    pygame.init()
    resolution : tuple[int, int] = (1280, 720)
    running : bool = True

    pygame.display.set_caption("Final Project")
    screen : pygame.Surface = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    viewport : pygame.Surface = pygame.surface.Surface((1920, 1080))

    test : pygame.Surface = pygame.surface.Surface((100, 100))
    test.fill((255, 0, 0))

    clock = pygame.time.Clock()
    fps = 60
    delta = 0

    while running:
        viewport.fill((0, 0, 0))
        viewport.blit(test, (50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(pygame.transform.scale(viewport, screen.get_rect().size), (0, 0))
        pygame.display.flip()
        delta = clock.tick(fps)
        
    sys.exit()


if __name__ == "__main__":
    main()