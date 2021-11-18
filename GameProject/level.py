# import libraries / files
from support import *
from settings import *


# class definition
class Level:

    # initialise class attributes
    def __init__(self, level_data, surface):
        self.screen = surface
        self.level_num = 1

        # background image
        self.level_background = pygame.image.load("Assets/BG1.png").convert_alpha()

        # gets the level csv data and adds it to this variable
        self.level_layout = import_level_data(level_data[f'{self.level_num}'])

        # array to hold the tile sprite and its coordinates
        self.tile_layout = []

        # sprite group for exit
        self.exit_sprite = pygame.sprite.Group()

        # load tile images
        dirt = pygame.image.load('Assets/Tiles/grassCenter.png').convert_alpha()
        grass = pygame.image.load('Assets/Tiles/grassMid.png').convert_alpha()
        log_platform = pygame.image.load('Assets/Tiles/bridgeLogs.png').convert_alpha()

        # enumerate - keeps track of how many iterations have occurred
        # goes through the y position
        for row_index, row in enumerate(self.level_layout):
            # goes through the x position
            for column_index, value in enumerate(row):

                # checks value of tile and assign specific tile sprite
                # calculates coordinates of tile
                if value == '152':
                    tile = pygame.transform.scale(dirt, (tile_size, tile_size))
                    tile_rect = tile.get_rect()
                    tile_rect.x = column_index * tile_size
                    tile_rect.y = row_index * tile_size
                    value = (tile, tile_rect)
                    self.tile_layout.append(value)

                elif value == '103':
                    tile = pygame.transform.scale(grass, (tile_size, tile_size))
                    tile_rect = tile.get_rect()
                    tile_rect.x = column_index * tile_size
                    tile_rect.y = row_index * tile_size
                    value = (tile, tile_rect)
                    self.tile_layout.append(value)

                elif value == '124':
                    tile = pygame.transform.scale(log_platform, (tile_size, (tile_size // 10) * 4))
                    tile_rect = tile.get_rect()
                    tile_rect.x = column_index * tile_size
                    tile_rect.y = row_index * tile_size
                    value = (tile, tile_rect)
                    self.tile_layout.append(value)

                elif value == '57':
                    tile = Exit(column_index * tile_size, row_index * tile_size - 40)
                    self.exit_sprite.add(tile)

    # method to run level
    def run(self):
        screen.blit(pygame.transform.scale(self.level_background, screen_size), (0, 0))
        # goes through the array
        for value in self.tile_layout:
            # draws each tile on screen
            screen.blit(value[0], value[1])


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Assets/Tiles/exit.png').convert_alpha()
        self.image = pygame.transform.scale(img, (tile_size, (tile_size + 40)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
