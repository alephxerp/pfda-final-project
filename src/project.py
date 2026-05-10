import pygame, sys, os
from element import Element, ElementGroup
from button import Button, ButtonGroup
from character import Character, CharacterGroup
from dialogue import DialogueManager
from mouse import Mouse


rendergroup : ElementGroup = ElementGroup()
rendergroup.set_background("background.png")
processgroup : ElementGroup = ElementGroup()

def add_render(elementgroup : ElementGroup) -> None:
    for element in elementgroup:
        element.add(rendergroup)

def remove_render(elementgroup : ElementGroup) -> None:
    for element in elementgroup:
        element.remove(rendergroup)

def change_render(elementgroup : ElementGroup) -> None:
    rendergroup.empty()
    add_render(elementgroup)

def add_process(elementgroup : ElementGroup) -> None:
    for element in elementgroup:
        element.add(processgroup)

def remove_process(elementgroup : ElementGroup) -> None:
    for element in elementgroup:
        element.remove(processgroup)

def change_process(elementgroup : ElementGroup) -> None:
    processgroup.empty()
    add_process(elementgroup)



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

    game : CharacterGroup = CharacterGroup()
    game.create("guy.png", ["i am number one guy"], (350, 350))
    game.create("guy.png", ["i am number two guy", "i speak twice"], (700, 200))
    game.create("guy.png", ["i am guy de french", "i speak french"], (1500, 950))

    add_render(game)
    add_process(game)

    menu : ButtonGroup = ButtonGroup()
    menutint : Element = Element("menu_tint.png", (960, 540))
    menutint.add(menu)

    menu.create("button_resume.png", print, position=(50, 50))
    menu.create("button_exit.png", sys.exit, position=(50, 300))

    paused : bool = False
    

    dialogue : DialogueManager = DialogueManager()
    dialoguegroup : ElementGroup = ElementGroup()
    dialogue.add(dialoguegroup)

    
    while running:
        viewport.fill((0, 0, 0))

        processgroup.process()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys : list[bool] = pygame.key.get_just_pressed()
        if keys[pygame.K_ESCAPE]:
            if paused == False:
                add_render(menu)
                change_process(menu)
                paused = True
            else:
                remove_render(menu)
                change_process(game)
                paused = False
        if keys[pygame.K_SPACE]:
            if dialogue.speaking:
                dialogue.on_click()
                if not dialogue.speaking:
                    remove_render(dialoguegroup)
                    change_process(game)
        

        mouse.update(viewport, screen)

        for element in processgroup:
            if element.rect.collidepoint(mouse.position):
                element.on_hover()

                if mouse.left_click or mouse.right_click:
                    # Janky temporary solution for resume button.
                    if type(element) is Button:
                        element.on_click()
                        if paused == False:
                            add_render(menu)
                            change_process(menu)
                            paused = True
                        else:
                            remove_render(menu)
                            change_process(game)
                            paused = False
                    
                    elif type(element) is Character:
                        dialogue.start(element.on_click())
                        add_render(dialoguegroup)
                        change_process(dialoguegroup)

                    elif type(element) is DialogueManager:
                        element.on_click()
                        if not element.speaking:
                            remove_render(dialoguegroup)
                            change_process(game)
        

        viewport.blit(rendergroup.render())

        screen.blit(pygame.transform.scale(viewport, screen.get_rect().size), (0, 0))
        pygame.display.flip()
        delta = clock.tick(fps)
        
    sys.exit()


if __name__ == "__main__":
    main()