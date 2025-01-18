import pygame
import pygame_gui
import logging
import json
from ui.menu import show_main_menu
from ui.map_selection import show_map_selection
from ui.play_uk_map import show_uk_map
from ui.pause import show_pause
from settings import *


# Initialize logging
logging.basicConfig(filename='game.log', level=logging.INFO, filemode='w')
logging.info('Game started')

# Initialize the settings
logging.info('Loading settings')
logging.info(f"FPS: {FPS}")
logging.info(f"Colors: {COLORS}")
logging.info(f"Audio settings: {AUDIO_SETTINGS}")
logging.info(f"Image settings: {IMAGE_SETTINGS}")
logging.info(f"Map settings: {MAP_SETTINGS}")
logging.info(f"Other settings: {OTHER_SETTINGS}")
logging.info('Settings loaded')

# Initialize pygame
pygame.init()

# Get screen resolution
def get_screen_resolution():
    display_info = pygame.display.Info()
    logging.info(f"Screen resolution: {display_info.current_w} x {display_info.current_h}")
    return display_info.current_w, display_info.current_h

SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()

# Save screen resolution to settings.json
with open('src/settings/settings.json', 'r+') as f:
    settings = json.load(f)
    settings['SCREEN_WIDTH'] = SCREEN_WIDTH
    settings['SCREEN_HEIGHT'] = SCREEN_HEIGHT
    f.seek(0)
    json.dump(settings, f, indent=4)
    f.truncate()

# Initialize window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scramble Game")

# FPS Clock
clock = pygame.time.Clock()
fps = FPS

# Initialize UI
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "src/assets/ui_theme.json")
logging.info("ui_theme.json loaded")

running = True
current_scene = "menu"

try:
    while running:
        time_delta = clock.tick(fps) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle UI events
            # Ici logique pour la scene "menu"
            if current_scene == "menu":
                next_scene = show_main_menu(event, manager)
                if next_scene == "map_selection":
                    current_scene = "map_selection"
                    manager.clear_and_reset()  # Réinitialiser l'écran

            # Ici logique pour la scene "map_selection"
            elif current_scene == "map_selection":
                next_scene = show_map_selection(event, manager)
                if next_scene == "menu":
                    current_scene = "menu"
                    manager.clear_and_reset()  # Réinitialiser l'écran
                elif next_scene == "play_uk_map":
                    logging.info("Playing UK map")
                    current_scene = "play_uk_map"
                    manager.clear_and_reset()
                elif next_scene == "play_france_map":
                    logging.info("Playing France map")
                    current_scene = "play_france_map"
                    manager.clear_and_reset()

            # Ici logique pour la scene "play_uk_map"
            elif current_scene == "play_uk_map":
                next_scene = show_uk_map(event, manager)
                if next_scene == "pause":
                    current_scene = "pause"
                    manager.clear_and_reset()
            
            # Ici logique pour la scene "play_france_map"
            elif current_scene == "play_france_map":
                pass

            # Ici logique pour la scene "pause"
            elif current_scene == "pause":
                next_scene = show_pause(event, manager)
                if next_scene == "play_uk_map":
                    current_scene = "play_uk_map"
                    manager.clear_and_reset()
                elif next_scene == "menu":
                    current_scene = "menu"
                    manager.clear_and_reset()
                elif next_scene == "quit":
                    running = False

            manager.process_events(event)

        # Effacer l'écran
        screen.fill(WHITE)

        # Mettre à jour l'interface utilisateur
        if current_scene == "menu":
            show_main_menu(None, manager, screen)

        elif current_scene == "map_selection":
            show_map_selection(None, manager, screen)

        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.flip()
except KeyboardInterrupt:
    logging.info('Game stopped by user')
    pygame.quit()

logging.info('Game ended')
pygame.quit()