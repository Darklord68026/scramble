import pygame_gui
from settings import *
from main import logging

ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "src/assets/ui_theme.json")
logging.info("ui_theme.json loaded")