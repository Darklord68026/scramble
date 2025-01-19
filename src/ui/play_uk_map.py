import pygame
import pygame_gui
from settings import *
from pygame.locals import *
from app_init import initialize_app

screen, ui_manager = initialize_app()

def show_uk_map(event, screen=None):
    if event:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return "pause"
            
    if screen:
        pass
    return None