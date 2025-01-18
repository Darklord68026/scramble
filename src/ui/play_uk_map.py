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
        pass
    return None