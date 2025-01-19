import pygame
import pygame_gui

def initialize_app():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Scramble")
    ui_manager = pygame_gui.UIManager((800, 600), "src/assets/ui_theme.json")
    return screen, ui_manager
