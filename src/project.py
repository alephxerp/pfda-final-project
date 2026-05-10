import pygame, sys, os
from element import Element, ElementGroup
from mouse import Mouse
from button import Button
from character import Character


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

    game : ElementGroup = ElementGroup()
    game.create("guy.png", (350, 350))
    game.create("guy.png", (700, 200))
    game.create("guy.png", (1500, 950))

    for element in game:
        element.add(rendergroup, processgroup)


    menu : ElementGroup = ElementGroup()
    resume : Button = Button("button_resume.png", print, position=(50, 50))
    exit : Button = Button("button_exit.png", sys.exit, position=(50, 300))
    menu.add(resume, exit)

    paused : bool = False
    
    while running:
        viewport.fill((0, 0, 0))

        processgroup.process()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys : list[bool] = pygame.key.get_just_pressed()
        if keys[pygame.K_ESCAPE]:
            if paused == False:
                for element in menu:
                    element.add(rendergroup, processgroup)
                for element in game:
                    element.remove(processgroup)
                paused = True
            else:
                for element in menu:
                    element.remove(rendergroup, processgroup)
                for element in game:
                    element.add(processgroup)
                paused = False
        

        mouse.update(viewport, screen)

        for element in processgroup:
            if element.rect.collidepoint(mouse.position):
                element.on_hover()

                if mouse.left_click or mouse.right_click:
                    # Janky temporary solution for resume button.
                    if type(element) is Button:
                        if paused == False:
                            for element in menu:
                                element.add(rendergroup, processgroup)
                            for element in game:
                                element.remove(processgroup)
                            paused = True
                        else:
                            for element in menu:
                                element.remove(rendergroup, processgroup)
                            for element in game:
                                element.add(processgroup)
                            paused = False
                    
                    elif type(element) is Character:
                        pass

                    else:
                        element.on_click()

        viewport.blit(rendergroup.render())

        screen.blit(pygame.transform.scale(viewport, screen.get_rect().size), (0, 0))
        pygame.display.flip()
        delta = clock.tick(fps)
        
    sys.exit()


if __name__ == "__main__":
    main()