import pygame, sys


def main():
    pygame.init()
    resolution : tuple[int, int] = (960, 540)
    running : bool = True

    pygame.display.set_caption("Final Project")
    screen : pygame.display = pygame.display.set_mode(resolution, pygame.SHOWN)

    clock = pygame.time.Clock()
    fps = 60
    delta = 0

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        delta = clock.tick(fps)
        
    sys.exit()


if __name__ == "__main__":
    main()