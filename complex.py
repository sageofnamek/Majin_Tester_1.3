import pygame
import os
import random

def display_starter_image(screen, starter_image_complex):
    scaled_image = pygame.transform.scale(starter_image_complex, (screen.get_width(), screen.get_height()))  # Scale the image to fit the screen
    screen.fill((0, 0, 0))  # Clear the screen by filling it with black
    screen.blit(scaled_image, (0, 0))  # Draw the image at the top-left corner
    pygame.display.update()  # Update the display to show the image

def load_images(images_folder):
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.png')]  # Load all PNG files
    images = [pygame.image.load(os.path.join(images_folder, f)) for f in image_files]
    return images

def display_random_image(screen, images):
    random_image = random.choice(images)  # Select a random image
    scaled_image = pygame.transform.scale(random_image, (screen.get_width(), screen.get_height()))  # Scale the image to fit the screen
    screen.fill((0, 0, 0))  # Clear the screen by filling it with black
    screen.blit(scaled_image, (0, 0))  # Draw the image at the top-left corner
    pygame.display.update()  # Update the display to show the image
