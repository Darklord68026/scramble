import pygame
from main import logging

def load_image(path):
    logging.info(f"Image {path} loaded")
    return pygame.image.load(path).convert_alpha()


def load_sound(path):
    logging.info(f"Sound {path} loaded")
    return pygame.mixer.Sound(path)