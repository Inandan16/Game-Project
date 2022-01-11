import pygame


class button:
    # initialise class attributes
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # draws button with collision
    def draw(self, surface) -> bool:

        # boolean to check if an action should be performed
        action = False

        # gets x and y coordinates of cursor
        mouse = pygame.mouse.get_pos()

        # checks for mouse click when cursor is in collision range
        # changes boolean if mouse pressed and if boolean hasn't been changed
        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        # changes boolean to false if mouse not pressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draws button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
