import pygame
import os
import sys
import random  # Import random for selecting random images
import colors  # Import the colors.py module
import simpleimages  # Import the simpleimages.py module

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
pygame.display.set_caption('Majin Tester')
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Load different starter images (now using .png extensions)
starter_image_color_path = resource_path('starterimage_color.png')
starter_image_simple_path = resource_path('starterimage_simple.png')
starter_image_complex_path = resource_path('starterimage_complex.png')

starter_image_color = pygame.image.load(starter_image_color_path)
starter_image_simple = pygame.image.load(starter_image_simple_path)
starter_image_complex = pygame.image.load(starter_image_complex_path)

# Load c1.png to c7.png images from the 'colors' folder
c_images = []
for i in range(1, 8):  # From c1 to c7
    image_path = resource_path(os.path.join('colors', f'c{i}.png'))
    image = pygame.image.load(image_path)
    c_images.append(image)

# Load v1.wav to v7.wav sounds from the 'voice colors' folder
voice_colors = []
for i in range(1, 8):  # From v1 to v7
    sound_path = resource_path(os.path.join('voice colors', f'v{i}.wav'))
    sound = pygame.mixer.Sound(sound_path)
    voice_colors.append(sound)

# Load 1.png to 10.png images from the 'simple images' folder
simple_images = []
for i in range(1, 11):  # From 1.png to 10.png
    image_path = resource_path(os.path.join('simple images', f'{i}.png'))
    image = pygame.image.load(image_path)
    simple_images.append(image)

# Load 1.wav to 10.wav sounds from the 'simple images audio' folder
simple_audio = []
for i in range(1, 11):  # From 1.wav to 10.wav
    sound_path = resource_path(os.path.join('simple images audio', f'{i}.wav'))
    sound = pygame.mixer.Sound(sound_path)
    simple_audio.append(sound)

# Load 1.png to 50.png images from the 'images' folder (complex images) and resize them to 683x683
complex_images = []
for i in range(1, 51):  # From 1.png to 50.png
    image_path = resource_path(os.path.join('images', f'{i}.png'))
    image = pygame.image.load(image_path)
    resized_image = pygame.transform.scale(image, (screen_width, screen_height))  # Resize to 683x683
    complex_images.append(resized_image)

# Function to create buttons
def create_button(text, x, y, width, height, color, hover_color, action=None):
    if not menu_active:  # Don't draw the button if the menu is not active
        return

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf = small_text.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surf, text_rect)

# Function to display any image
def display_image(image):
    screen.blit(image, (0, 0))
    pygame.display.update()

# Actions for buttons
def show_colors():
    global menu_active
    menu_active = False  # Disable the menu
    colors.display_starter_image(screen, starter_image_color)  # Display the starter image for colors
    global in_colors_mode
    in_colors_mode = True
    global in_simple_mode
    in_simple_mode = False
    global in_complex_mode
    in_complex_mode = False

def show_simple_images():
    global menu_active
    menu_active = False  # Disable the menu
    simpleimages.display_starter_image(screen, starter_image_simple)  # Display the starter image for simple images
    global in_simple_mode
    in_simple_mode = True
    global in_colors_mode
    in_colors_mode = False
    global in_complex_mode
    in_complex_mode = False

def show_complex_images():
    global menu_active
    menu_active = False  # Disable the menu
    display_image(starter_image_complex)  # Display the starter image for complex images
    global in_complex_mode
    in_complex_mode = True
    global in_colors_mode
    in_colors_mode = False
    global in_simple_mode
    in_simple_mode = False

# Function to display the menu
def show_menu():
    # Load the background image
    background_image_path = resource_path('background.png')
    background_image = pygame.image.load(background_image_path)

    while menu_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Scale the background image to fit the screen
        scaled_background = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(scaled_background, (0, 0))  # Blit the background image to cover the entire screen

        # Create buttons
        button_width = 200
        button_height = 50
        gap = 20
        start_y = (screen_height - (button_height * 3 + gap * 2)) // 2
        create_button('Colors', (screen_width - button_width) // 2, start_y, button_width, button_height, (100, 100, 100), (150, 150, 150), show_colors)
        create_button('Simple Images', (screen_width - button_width) // 2, start_y + button_height + gap, button_width, button_height, (100, 100, 100), (150, 150, 150), show_simple_images)
        create_button('Complex Images', (screen_width - button_width) // 2, start_y + (button_height + gap) * 2, button_width, button_height, (100, 100, 100), (150, 150, 150), show_complex_images)

        pygame.display.update()

# Main loop
menu_active = True
in_colors_mode = False
in_simple_mode = False
in_complex_mode = False
current_image_index = None
show_menu()  # Show the menu first

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_active = True  # Activate the menu when ESC is pressed
                show_menu()  # Show the menu
            elif event.key == pygame.K_SPACE and in_colors_mode:
                colors.display_starter_image(screen, starter_image_color)  # Display starter image for colors when spacebar is pressed
            elif event.key == pygame.K_SPACE and in_simple_mode:
                simpleimages.display_starter_image(screen, starter_image_simple)  # Display starter image for simple images when spacebar is pressed
            elif event.key == pygame.K_SPACE and in_complex_mode:
                display_image(starter_image_complex)  # Display starter image for complex images when spacebar is pressed
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER) and in_colors_mode:
                current_image_index = colors.display_random_c_image(screen, c_images)  # Display a random c1.png to c7.png image
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER) and in_simple_mode:
                current_image_index = simpleimages.display_random_simple_image(screen, simple_images)  # Display a random simple image
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER) and in_complex_mode:
                current_image_index = random.randint(0, len(complex_images) - 1)
                display_image(complex_images[current_image_index])  # Display a random complex image
            elif event.key in (pygame.K_1, pygame.K_KP1) and in_colors_mode and current_image_index is not None:
                colors.play_voice_color(voice_colors, current_image_index)  # Play the corresponding .wav file for colors
            elif event.key in (pygame.K_1, pygame.K_KP1) and in_simple_mode and current_image_index is not None:
                simpleimages.play_simple_image_audio(simple_audio, current_image_index)  # Play the corresponding .wav file for simple images
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            if not menu_active:
                display_image(starter_image_color)  # Re-display the starter image on resize
            if in_colors_mode:
                colors.display_starter_image(screen, starter_image_color)  # Re-display the starter image on resize in Colors mode
            if in_simple_mode:
                simpleimages.display_starter_image(screen, starter_image_simple)  # Re-display the starter image on resize in Simple Images mode
            if in_complex_mode:
                display_image(starter_image_complex)  # Re-display the starter image on resize in Complex Images mode

# Quit pygame
pygame.quit()
