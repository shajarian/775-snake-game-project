import pygame
import sys
import os

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Constants
FRUIT_SOUNDS_FOLDER = 'fruit-rap'

# Load fruit sounds
FRUIT_SOUNDS = {
    "apple": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'apple.mp3')),
    "banana": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'banana.mp3')),
    "grapes": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'grapes.mp3')),
    "watermelon": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'watermelon.mp3')),
    "orange": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'orange.mp3')),
    "pineapple": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'pineapple.mp3')),
    "cherries": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'cherries.mp3')),
    "lemon": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'lemon.mp3')),
    "coconut": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'coconut.mp3')),
}

# Convert the dictionary to a list of sounds
sounds = list(FRUIT_SOUNDS.values())
current_sound_index = 0

# Function to play a sound
def play_sound(index):
    # Stop all sounds before playing the new one
    for sound in sounds:
        sound.stop()
    sounds[index].play()

# Set up the screen
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Fruit Sound Player")

# Start playing the first sound
play_sound(current_sound_index)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_sound_index = (current_sound_index + 1) % len(sounds)
                play_sound(current_sound_index)
            elif event.key == pygame.K_LEFT:
                current_sound_index = (current_sound_index - 1) % len(sounds)
                play_sound(current_sound_index)

    screen.fill((0, 0, 0))  # Clear the screen
    pygame.display.flip()  # Update the screen

pygame.quit()
sys.exit()
