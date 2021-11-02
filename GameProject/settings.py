# imports pygame
# files that import this file will be able to use these imports as well
import pygame, sys
from pygame.locals import *

# tile variables
vertical_tiles = 13
horizontal_tiles = 22
tile_size = 70


# text function
# this will allow for text to be drawn on top of images that have been loaded in
def draw_text(text, font, color, surface, x, y):
    object_text = font.render(text, 1, color)
    text_rect = object_text.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(object_text, text_rect)


# sets game window size
screen_size = [(horizontal_tiles * tile_size), (vertical_tiles * tile_size)]

# window dimensions and caption
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game")
