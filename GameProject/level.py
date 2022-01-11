# import libraries / files
from support import *
from settings import *


# class definition
class Level:

    # initialise class attributes
    def __init__(self, level_data, level_num):

        # background image
        self.level_background = pygame.image.load("Assets/BG1.png").convert_alpha()

        # gets the level csv data and adds it to this variable
        level_layout = import_level_data(level_data[f"{level_num}"])

        # array to hold the tile sprite and its coordinates
        self.tile_layout = []

        # sprite groups
        self.exit_sprite = pygame.sprite.Group()
        self.lava_sprite = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()

        # load tile images
        dirt = pygame.image.load("Assets/Tiles/grassCenter.png").convert_alpha()
        grass = pygame.image.load("Assets/Tiles/grassMid.png").convert_alpha()
        log_platform = pygame.image.load("Assets/Tiles/bridgeLogs.png").convert_alpha()

        # coin icon for score
        score_coin = Coin(0, 0)
        self.coin_group.add(score_coin)

        # enumerate - keeps track of how many iterations have occurred
        # goes through the y position
        for row_index, row in enumerate(level_layout):
            # goes through the x position
            for column_index, value in enumerate(row):

                # checks value of tile and assign specific tile sprite
                # calculates coordinates of tile
                if value == "152":
                    tile = pygame.transform.scale(dirt, (tile_size, tile_size))
                    tile_rect = tile.get_rect()
                    tile_rect.x = column_index * tile_size
                    tile_rect.y = row_index * tile_size
                    value = (tile, tile_rect)
                    self.tile_layout.append(value)

                elif value == "103":
                    tile = pygame.transform.scale(grass, (tile_size, tile_size))
                    tile_rect = tile.get_rect()
                    tile_rect.x = column_index * tile_size
                    tile_rect.y = row_index * tile_size
                    value = (tile, tile_rect)
                    self.tile_layout.append(value)

                elif value == "124":
                    tile = pygame.transform.scale(
                        log_platform, (tile_size, (tile_size // 10) * 4)
                    )
                    tile_rect = tile.get_rect()
                    tile_rect.x = column_index * tile_size
                    tile_rect.y = row_index * tile_size
                    value = (tile, tile_rect)
                    self.tile_layout.append(value)

                elif value == "57":
                    tile = Exit(column_index * tile_size, row_index * tile_size - 40)
                    self.exit_sprite.add(tile)

                elif value == "138":
                    tile = Lava(column_index * tile_size, row_index * tile_size + (tile_size // 2))
                    self.lava_sprite.add(tile)

                elif value == "0":
                    tile = Coin(column_index * tile_size, row_index * tile_size)
                    self.coin_group.add(tile)

                elif value == "15":
                    tile = Platform(column_index * tile_size, row_index * tile_size, 1, 0)
                    self.platform_group.add(tile)

                elif value == "80":
                    tile = Platform(column_index * tile_size, row_index * tile_size, 0, 1)
                    self.platform_group.add(tile)

                elif value == "6":
                    tile = Enemy(column_index * tile_size, row_index * tile_size + 35)
                    self.enemy_group.add(tile)

    # method to run level
    def run(self):
        screen.blit(pygame.transform.scale(self.level_background, screen_size), (0, 0))
        # goes through the array
        for value in self.tile_layout:
            # draws each tile on screen
            screen.blit(value[0], value[1])


# subclasses of pygame's sprite class
# allows all instances of these classes to use spritecollide method
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Assets/Tiles/exit.png").convert_alpha()
        self.image = pygame.transform.scale(img, (tile_size, (tile_size + 40)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Assets/Tiles/lava.png").convert_alpha()
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 4 * 3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Assets/Tiles/coinGold.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Assets/enemy.png")
        self.image = pygame.transform.scale(img, (tile_size - 10, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 105:
            self.move_direction *= -1
            self.move_counter *= -1


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Assets/Tiles/bridgeLogs.png")
        self.image = pygame.transform.scale(img, (tile_size, (tile_size // 10) * 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 140:
            self.move_direction *= -1
            self.move_counter *= -1

