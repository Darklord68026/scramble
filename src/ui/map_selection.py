import pygame
import pygame_gui
from settings import *
from main import logging

def show_map_selection(event, manager, screen=None):
    if event:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element.text == "Retour":
                    return "menu"
                elif event.ui_element.text == "Map Royaume-Uni":
                    return "play_uk_map"
                elif event.ui_element.text == "Map France":
                    return "play_france_map"
                
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
            text="Sélectionnez une carte",
            manager=manager,
            object_id="#map-selection-label"
        )

        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - 200) // 2 - 250, (SCREEN_HEIGHT - 50) // 2),
                (button_width, button_height)
            ),
            text="Map Royaume-Uni",
            manager=manager,
            object_id="#uk-map-button"
        )
        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 50) // 2),
                (button_width, button_height)
            ),
            text="Map France",
            manager=manager,
            object_id="#fr-map-button"
        )
        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                ((SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 50) // 2 + 100),
                (button_width, button_height)
            ),
            text="Retour",
            manager=manager,
            object_id="#back-button"
        )
    return None
        # TODO : Implémenter les autres cartes selon la meme méthode
