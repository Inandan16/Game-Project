from level import *
from game_data import levels


# player class
class Player:
    def __init__(self, x, y, level_num):
        # list to hold images for character animation walking
        self.player_right = []
        self.player_left = []
        self.player_jump_right = []
        self.player_jump_left = []
        self.index = 0
        # the number of iterations that has been done (needed for adjusting animation speed)
        self.counter = 0
        # instance of level class - needed for collision
        if level_num < 6:
            self.level = Level(levels, level_num)
        else:
            level_num = 1
            self.level = Level(levels, level_num)
        # player hurt sprite
        self.player_hurt = pygame.image.load(
            "Assets/Player/Char 1/oneHurt.png"
        ).convert_alpha()

        # for loop allows it to cycle through the different pngs
        for num in range(1, 12):
            # import in player sprite
            # f = formats the string so that the number can be cycled through - used for animation
            image_right = pygame.image.load(
                f"Assets/Player/Char 1/onewalk{num}.png"
            ).convert_alpha()
            # fit player to tiles
            image_right = pygame.transform.scale(
                image_right, (tile_size, tile_size + (tile_size // 2))
            )
            # flip has three parameters = surface, bool to flip surface in x axis and bool to flip surface in y axis
            image_left = pygame.transform.flip(image_right, True, False)
            image_jump_right = pygame.image.load(
                "Assets/Player/Char 1/oneJump.png"
            ).convert_alpha()
            image_jump_right = pygame.transform.scale(
                image_jump_right, (tile_size, tile_size + (tile_size // 2))
            )
            image_jump_left = pygame.transform.flip(image_jump_right, True, False)
            self.player_right.append(image_right)
            self.player_left.append(image_left)
            self.player_jump_right = image_jump_right
            self.player_jump_left = image_jump_left

        self.player_sprite = self.player_right[self.index]
        self.rect = self.player_sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.player_sprite.get_width()
        self.height = self.player_sprite.get_height()
        self.player_y_velocity = 0
        self.jumped = False
        self.direction = 1
        self.airbourne = True

    def update(self, state):

        # local variables for method
        # coordinate changes - will make collision calculations easier
        x_change = 0
        y_change = 0
        # variable to say that 1 iterations need to pass before index is updated
        # slows the animation down, stopping the iterations from causing to cycle through as fast as it can
        walk_cooldown = 1
        # checks for collision within set number of pixels if player is below platform
        collision_threshold = 20

        if state == 1:

            # keypress check
            key = pygame.key.get_pressed()

            # checks if key is pressed and player hasn't jumped
            if key[pygame.K_UP] and not self.jumped and not self.airbourne:
                self.player_y_velocity = -18
                self.jumped = True
            if not key[pygame.K_UP]:
                self.jumped = False
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
            if self.airbourne and self.direction == 1:
                self.player_sprite = self.player_jump_right
            if self.airbourne and self.direction == -1:
                self.player_sprite = self.player_jump_left

            # player gravity
            self.player_y_velocity += 1

            # terminal velocity (max gravity)
            if self.player_y_velocity > 10:
                self.player_y_velocity = 10

            # velocity the player goes up
            y_change += self.player_y_velocity

            # collision check
            # variable saying whether player is in the air
            self.airbourne = True
            for tile in self.level.tile_layout:
                # collision check in x direction
                if tile[1].colliderect(
                    self.rect.x + x_change,
                    self.rect.y,
                    self.width,
                    self.height,
                ):
                    x_change = 0
                # collision check in y direction
                if tile[1].colliderect(
                    self.rect.x,
                    self.rect.y + y_change,
                    self.width,
                    self.height,
                ):
                    # below tile collision (jumping)
                    if self.player_y_velocity < 0:
                        y_change = tile[1].bottom - self.rect.top
                        self.player_y_velocity = 0
                    # above tile collision (falling)
                    elif self.player_y_velocity >= 0:
                        y_change = tile[1].top - self.rect.bottom
                        self.player_y_velocity = 0
                        self.airbourne = False

            # exit collision
            if pygame.sprite.spritecollide(self, self.level.exit_sprite, False):
                state = 2

            # lava collision
            if pygame.sprite.spritecollide(self, self.level.lava_sprite, False):
                state = -1

            # enemy collision
            self.level.enemy_group.update()
            if pygame.sprite.spritecollide(self, self.level.enemy_group, False):
                state = -1

            # collision check with platform
            self.level.platform_group.update()
            for platform in self.level.platform_group:

                # collision in x direction
                if platform.rect.colliderect(
                    self.rect.x + x_change, self.rect.y, self.width, self.height
                ):
                    x_change = 0

                # collision in y direction
                if platform.rect.colliderect(
                    self.rect.x, self.rect.y + y_change, self.width, self.height
                ):

                    # check if below platform
                    if (
                        abs((self.rect.top + y_change) - platform.rect.bottom)
                        < collision_threshold
                    ):
                        self.player_y_velocity = 0
                        y_change = platform.rect.bottom - self.rect.top

                    # check if above platform
                    elif (
                        abs((self.rect.bottom + y_change) - platform.rect.top)
                        < collision_threshold
                    ):
                        self.rect.bottom = platform.rect.top - 1
                        self.airbourne = False
                        y_change = 0

                    # moving player relative to platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

            # player coord updates
            self.rect.x += x_change
            self.rect.y += y_change

        if state == -1:

            self.player_sprite = self.player_hurt

            if self.direction == -1:
                self.player_sprite = pygame.transform.flip(
                    self.player_sprite, True, False
                )

            draw_text(
                "Try again?",
                pixel_font,
                (255, 255, 255),
                screen,
                screen_size[0] // 2,
                screen_size[1] // 2 - 100,
            )

        # draws player on screen
        screen.blit(self.player_sprite, self.rect)

        return state
