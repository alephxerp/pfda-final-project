import pygame, sys, os
from element import Element
from mouse import Mouse


def main() -> None:
    pygame.init()
    resolution : tuple[int, int] = (1280, 720)
    running : bool = True

    pygame.display.set_caption("Final Project")
    screen : pygame.Surface = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    viewport : pygame.Surface = pygame.surface.Surface((1920, 1080))

    mouse : Mouse = Mouse()

    clock = pygame.time.Clock()
    fps = 60
    delta = 0


    test : Element = Element((50, 50), "guy.png")


    while running:
        viewport.fill((0, 0, 0))
        viewport.blit(test.image, (50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        mouse.update(viewport, screen)

        if mouse.left_click:
            print("left clicked!")
        if mouse.right_click:
            print("right clicked!")

        if test.rect.collidepoint(mouse.position): 
            test.on_hover()

            if mouse.left_click or mouse.right_click:
                test.on_click()

        screen.blit(pygame.transform.scale(viewport, screen.get_rect().size), (0, 0))
        pygame.display.flip()
        delta = clock.tick(fps)
        
    sys.exit()


if __name__ == "__main__":
    main()