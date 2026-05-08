import pygame, sys, os


class Element(pygame.sprite.Sprite):
    def __init__(self, position : tuple[int, int], sprite : str) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.position : tuple[int, int] = position

        self.image : pygame.Surface = pygame.image.load(os.path.join("assets", sprite)).convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect()
        self.rect.center = position

        self.dead : bool = False


    def update(self) -> None:
        pass





def main() -> None:
    pygame.init()
    resolution : tuple[int, int] = (1280, 720)
    running : bool = True

    pygame.display.set_caption("Final Project")
    screen : pygame.Surface = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    viewport : pygame.Surface = pygame.surface.Surface((1920, 1080))

    test : Element = Element((50, 50), "guy.png")

    clock = pygame.time.Clock()
    fps = 60
    delta = 0

    while running:
        viewport.fill((0, 0, 0))
        viewport.blit(test.image, (50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(pygame.transform.scale(viewport, screen.get_rect().size), (0, 0))
        pygame.display.flip()
        delta = clock.tick(fps)
        
    sys.exit()


if __name__ == "__main__":
    main()