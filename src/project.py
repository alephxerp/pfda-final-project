import pygame, sys


class Mouse():
    def __init__(self):
        self.position = [0, 0]

    def update():
        pass


class Button():
    def __init__(self):
        self.position : tuple[int, int] = (0, 0)



def main():
    pygame.init()
    resolution : tuple[int, int] = (1280, 720)
    running : bool = True

    pygame.display.set_caption("Final Project")
    screen : pygame.Surface = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    viewport : pygame.Surface = screen.copy()

    clock = pygame.time.Clock()
    fps = 60
    delta = 0

    while running:
        viewport.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(pygame.transform.scale(viewport, screen.get_rect().size), (0, 0))
        pygame.display.flip()
        delta = clock.tick(fps)
        
    sys.exit()


if __name__ == "__main__":
    main()