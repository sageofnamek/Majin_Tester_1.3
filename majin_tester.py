import pygame
import os
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 683
screen_height = 683

# Function to get the absolute path to the resource (images folder and icon)
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Set window icon
icon_path = resource_path('icon.png')
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

# Set window title and dimensions
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('Random Image Viewer')

# Load starter image
starter_image_path = resource_path('starterimage.jpg')
starter_image = pygame.image.load(starter_image_path)

# Load images from the images folder
image_folder = resource_path('images')
image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
images = [pygame.image.load(os.path.join(image_folder, f)) for f in image_files]

# Function to display a given image
def display_image(image):
    scaled_image = pygame.transform.scale(image, (683, 683))  # Scale to screen dimensions
    screen.fill((0, 0, 0))  # Fill the screen with black before blitting the image
    screen.blit(scaled_image, (0, 0))  # Display the image at the top-left corner
    pygame.display.update()

# Function to display a random image from the list
def display_random_image():
    random_image = random.choice(images)
    display_image(random_image)

# Main loop
running = True
display_image(starter_image)  # Display the starter image initially
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                display_random_image()
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            display_image(starter_image)  # Re-display the starter image on resize

# Quit pygame
pygame.quit()
