import pygame, sys, os
from element import Element, ElementGroup
from mouse import Mouse


def main() -> None:
    pygame.init()
    resolution : tuple[int, int] = (1280, 720)
    running : bool = True

    pygame.display.set_caption("Final Project")
    screen : pygame.Surface = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    viewport : pygame.Surface = pygame.Surface((1920, 1080))

    mouse : Mouse = Mouse()

    clock = pygame.time.Clock()
    fps = 60
    delta = 0


    rendergroup : ElementGroup = ElementGroup()
    processgroup : ElementGroup = ElementGroup()

    guy : Element = Element("guy.png", (350, 350))
    guy.add(rendergroup, processgroup)

    rendergroup.create("tree.png", (1000, 1000))


    while running:
        viewport.fill((0, 0, 0))

        processgroup.process()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        mouse.update(viewport, screen)

        for element in processgroup:
            if element.rect.collidepoint(mouse.position):
                element.on_hover()

                if mouse.left_click or mouse.right_click:
                    element.on_click()

        rendergroup.render()
        viewport.blit(rendergroup.image, rendergroup.position)

        screen.blit(pygame.transform.scale(viewport, screen.get_rect().size), (0, 0))
        pygame.display.flip()
        delta = clock.tick(fps)
        
    sys.exit()


if __name__ == "__main__":
    main()