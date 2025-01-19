import pygame
import pygame_gui
from settings import *
from main import logging
from pygame.locals import *

def show_pause(event, manager, screen=None):
    if event:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return "play_uk_map"
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element.text == "Retour":
                    return "play_uk_map"
                elif event.ui_element.text == "Menu":
                    return "menu"
                elif event.ui_element.text == "Quitter":
                    pygame.quit()
                    exit()
    
    if screen:
        # Draw a semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)  # Set transparency level to 50%
        overlay.fill((0, 0, 0))  # Fill with black color
        screen.blit(overlay, (0, 0))

        label_width, label_height = 300, 50
        button_width, button_height = 200, 50

        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - label_width) // 2, (SCREEN_HEIGHT - label_height) // 2 - 100),
                (label_width, label_height)
            ),
            text="Pause",
            manager=manager,
            object_id="#pause-label"
        )
        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 50) // 2),
                (button_width, button_height)
            ),
            text="Retour",
            manager=manager,
            object_id="#resume-button"
        )
        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 50) // 2 + 100),
                (button_width, button_height)
            ),
            text="Menu",
            manager=manager,
            object_id="#menu-button"
        )
        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 50) // 2 + 200),
                (button_width, button_height)
            ),
            text="Quitter",
            manager=manager,
            object_id="#quit-button"
        )
    return None