import pygame_gui
import pygame
from settings import *

def show_main_menu(event, manager, screen=None):
    if event:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element.text == "Jouer":
                    return "map_selection"
                elif event.ui_element.text == "Quitter":
                    pygame.quit()
                    exit()
            
    if screen:
        # Charger l'image de fond
        background_image = pygame.image.load(BACKGROUND)
        resized_background = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_background, (0, 0))

        label_width, label_height = 300, 50
        button_width, button_height = 200, 50

        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - label_width) // 2, (SCREEN_HEIGHT - label_height) // 2 - 100),
                (label_width, label_height)
            ),
            text="Menu Principal",
            manager=manager,
            object_id="#menu-label"
        )
        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - button_width) // 2, (SCREEN_HEIGHT - button_height) // 2),
                (button_width, button_height)
            ),
            text="Jouer",
            manager=manager,
            object_id="#play-button"
        )
        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - button_width) // 2, (SCREEN_HEIGHT - button_height) // 2 + 100),
                (button_width, button_height)
            ),
            text="Quitter",
            manager=manager,
            object_id="#quit-button"
        )
    return None