import json

def load_settings():
    with open('src/settings/settings.json', 'r') as file:
        settings = json.load(file)
    return settings

settings = load_settings()

# Screen settings
FPS = settings["FPS"]
SCREEN_WIDTH = settings["SCREEN_WIDTH"]
SCREEN_HEIGHT = settings["SCREEN_HEIGHT"]

# Colors settings
COLORS = settings["COLORS"]
WHITE = COLORS["WHITE"]
BLACK = COLORS["BLACK"]
RED = COLORS["RED"]
GREEN = COLORS["GREEN"]
BLUE = COLORS["BLUE"]

# Audio settings
AUDIO_SETTINGS = settings["AUDIO_SETTINGS"]

# Image settings
IMAGE_SETTINGS = settings["IMAGE_SETTINGS"]
BACKGROUND = IMAGE_SETTINGS["BACKGROUND_IMAGE"]
CIVILIAN_AIRCRAFT = IMAGE_SETTINGS["CIVILIAN_AIRCRAFT"]
EUROFIGHTER_TYPHOON = IMAGE_SETTINGS["EUROFIGHTER_TYPHOON"]
F35 = IMAGE_SETTINGS["F35_LIGHTNING"]
F22 = IMAGE_SETTINGS["F22_RAPTOR"]
ENEMY_AIRCRAFT = IMAGE_SETTINGS["ENEMY_AIRCRAFT"]

# Map settings
MAP_SETTINGS = settings["MAP_SETTINGS"]
UK_MAP = MAP_SETTINGS["UK_MAP"]
FR_MAP = MAP_SETTINGS["FR_MAP"]

# Other settings
OTHER_SETTINGS = settings["OTHER_SETTINGS"]
TITLE = OTHER_SETTINGS["TITLE"]
APP_ICON = OTHER_SETTINGS["APP_ICON"]
