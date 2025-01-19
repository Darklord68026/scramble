import pygame
import pygame_gui
from settings import *
from main import logging
from pygame.locals import *

def show_uk_map(event, manager, screen=None):
    if event:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return "pause"
            
    if screen:
        background_image = pygame.image.load(UK_MAP)
        resized_background = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_background, (0, 0))
    return None