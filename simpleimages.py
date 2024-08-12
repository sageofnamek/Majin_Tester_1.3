# simpleimages.py

import pygame
import random

# Initialize the pygame mixer for sound playback
pygame.mixer.init()

# Function to display the starter image
def display_starter_image(screen, starter_image):
    scaled_image = pygame.transform.scale(starter_image, (screen.get_width(), screen.get_height()))  # Scale to screen dimensions
    screen.fill((0, 0, 0))  # Fill the screen with black before blitting the image
    screen.blit(scaled_image, (0, 0))  # Display the image at the top-left corner
    pygame.display.update()

# Function to display a random image from the simple images folder and return the image index
def display_random_simple_image(screen, simple_images):
    random_index = random.randint(0, len(simple_images) - 1)
    random_image = simple_images[random_index]
    scaled_image = pygame.transform.scale(random_image, (screen.get_width(), screen.get_height()))  # Scale to screen dimensions
    screen.fill((0, 0, 0))  # Fill the screen with black before blitting the image
    screen.blit(scaled_image, (0, 0))  # Display the image at the top-left corner
    pygame.display.update()
    return random_index

# Function to play the corresponding .wav file when the '1' key is pressed
def play_simple_image_audio(simple_audio, image_index):
    sound = simple_audio[image_index]
    sound.play()
