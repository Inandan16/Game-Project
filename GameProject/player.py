from level import *
from game_data import levels


# player class
class Player:
    def __init__(self, x, y):
        # list to hold images for character animation walking
        self.player_right = []
        self.player_left = []
        self.player_jump_right = []
        self.player_jump_left = []
        self.index = 0
        # the number of iterations that has been done (needed for adjusting animation speed)
        self.counter = 0
        # instance of level class - needed for collision
        self.level = Level(levels, screen_size)

        # for loop allows it to cycle through the different pngs
        for num in range(1, 12):
            # import in player sprite
            # f = formats the string so that the number can be cycled through - used for animation
            image_right = pygame.image.load(f'Assets/Player/Char 1/onewalk{num}.png').convert_alpha()
            # fit player to tiles
            image_right = pygame.transform.scale(image_right, (tile_size, tile_size + (tile_size // 2)))
            # flip has three parameters = surface, bool to flip surface in x axis and bool to flip surface in y axis
            image_left = pygame.transform.flip(image_right, True, False)
            image_jump_right = pygame.image.load('Assets/Player/Char 1/oneJump.png').convert_alpha()
            image_jump_right = pygame.transform.scale(image_jump_right, (tile_size, tile_size + (tile_size // 2)))
            image_jump_left = pygame.transform.flip(image_jump_right, True, False)
            self.player_right.append(image_right)
            self.player_left.append(image_left)
            self.player_jump_right = image_jump_right
            self.player_jump_left = image_jump_left

        self.player_sprite = self.player_right[self.index]
        self.rect = self.player_sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player_width = self.player_sprite.get_width()
        self.player_height = self.player_sprite.get_height()
        self.player_y_velocity = 0
        self.jumped = False
        self.direction = 1

    def update(self, state):

        # local variables for method
        # coordinate changes - will make collision calculations easier
        x_change = 0
        y_change = 0
        # variable to say that 1 iterations need to pass before index is updated
        # slows the animation down, stopping the iterations from causing to cycle through as fast as it can
        walk_cooldown = 1

        # keypress check
        key = pygame.key.get_pressed()

        # checks if key is pressed and player hasn't jumped
        if key[pygame.K_UP] and not self.jumped:
            self.player_y_velocity = -18
            self.jumped = True
        # check which direction key is pressed
        if key[pygame.K_LEFT]:
            x_change -= 10
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            x_change += 10
            self.counter += 1
            self.direction = 1
        # returns player sprite to neutral stand if not moving
        if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.player_sprite = self.player_right[self.index]
            if self.direction == -1:
                self.player_sprite = self.player_left[self.index]

        # player animation
        # walking animation inside this if statement to stop it overlapping with jumping animation
        if not self.jumped:
            # slows animation down to change every 2 iterations instead of every iteration
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.player_right):
                    self.index = 0
                if self.direction == 1:
                    self.player_sprite = self.player_right[self.index]
                if self.direction == -1:
                    self.player_sprite = self.player_left[self.index]
        if self.jumped and self.direction == 1:
            self.player_sprite = self.player_jump_right
        if self.jumped and self.direction == -1:
            self.player_sprite = self.player_jump_left

        # player gravity
        self.player_y_velocity += 1

        # terminal velocity (max gravity)
        if self.player_y_velocity > 10:
            self.player_y_velocity = 10

        # velocity the player goes up
        y_change += self.player_y_velocity

        # collision check
        for tile in self.level.tile_layout:
            # collision check in x direction
            if tile[1].colliderect(self.rect.x + x_change, self.rect.y, self.player_width,
                                   self.player_height):
                x_change = 0
            # collision check in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + y_change, self.player_width,
                                   self.player_height):
                # below tile collision (jumping)
                if self.player_y_velocity < 0:
                    y_change = tile[1].bottom - self.rect.top
                    self.player_y_velocity = 0
                # above tile collision (falling)
                elif self.player_y_velocity >= 0:
                    y_change = tile[1].top - self.rect.bottom
                    self.player_y_velocity = 0
                    self.jumped = False

        # exit collision
        if pygame.sprite.spritecollide(self, self.level.exit_sprite, False):
            state = 2

        # player coord updates
        self.rect.x += x_change
        self.rect.y += y_change

        # draws player on screen
        screen.blit(self.player_sprite, self.rect)

        return state
