import pygame, sys, os


class Element(pygame.sprite.Sprite):
    def __init__(self, position : tuple[int, int], sprite : str) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.position : tuple[int, int] = position

        self.image : pygame.Surface = pygame.image.load(os.path.join("assets", sprite)).convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect()
        self.rect.topleft = self.position

        self.dead : bool = False


    def on_hover(self) -> None:
        print("Hovering.")

    
    def on_click(self) -> None:
        if self.dead:
            self.image = pygame.image.load(os.path.join("assets", "tree.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        
        self.dead = ~self.dead
        print("I have been clicked!")


    def update(self) -> None:
        pass


class Mouse:
    position : tuple[int, int] = (0, 0)
    left_click = False
    right_click = False


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
        

        mouse.position = pygame.mouse.get_pos()
        mouse.left_click = pygame.mouse.get_just_pressed()[0]
        mouse.right_click = pygame.mouse.get_just_pressed()[2]

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