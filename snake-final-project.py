import psutil
import pygame
import sys
import random
import os
import time

# Initialize Pygame and its mixer
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

fruit_sound_channel = pygame.mixer.Channel(1)  # Allocate channel 1 for fruit sounds
pygame.mixer.music.set_volume(0.5)  # Set background music volume to 50%
fruit_sound_channel.set_volume(1.0)  # Set volume to maximum for the fruit sound channel


# Constants
BACKGROUND_MUSIC = "snake-background.mp3"
FRUIT_SOUNDS_FOLDER = 'fruit-rap/'
WIDTH, HEIGHT = 640, 480
PANEL_HEIGHT = 60
GAME_HEIGHT = HEIGHT - PANEL_HEIGHT
GRID_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FONT = pygame.font.Font(None, 24)
HIGH_SCORE_FILE = "highscore.txt"
EMOJI_FOLDER = "emoji-images/imgs"
TITLE_SCREEN_IMAGE = "snake-game-image.png"  # Replace with your image path

FRUIT_SIZE = (GRID_SIZE, GRID_SIZE)
# Game states
MENU = 0
GAME = 1
game_state = MENU

# Load background music
if os.path.exists(BACKGROUND_MUSIC):
    pygame.mixer.music.load(BACKGROUND_MUSIC)
    pygame.mixer.music.play(-1)
else:
    print(f"Unable to find music file: {BACKGROUND_MUSIC}")

# Load fruit images
FRUIT_IMAGES = {
    "🍎": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f34e.png')), FRUIT_SIZE),  # Apple
    "🍌": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f34c.png')), FRUIT_SIZE),  # Banana
    "🍇": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f347.png')), FRUIT_SIZE),  # Grapes
    "🍉": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f349.png')), FRUIT_SIZE),  # Watermelon
    "🍊": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f34a.png')), FRUIT_SIZE),  # Orange
    "🍍": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f34d.png')), FRUIT_SIZE),  # Pineapple
    "🍒": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f352.png')), FRUIT_SIZE),  # Cherries
    #"🍓": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f353.png')), FRUIT_SIZE),  # Strawberry
    "🍋": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f34b.png')), FRUIT_SIZE),  # Lemon
    "🥥": pygame.transform.scale(pygame.image.load(os.path.join(EMOJI_FOLDER, '1f965.png')), FRUIT_SIZE),  # Coconut
}


# Load fruit sounds
FRUIT_SOUNDS = {
    "apple": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'apple.mp3')),
    "banana": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'banana.mp3')),
    "grapes": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'grapes.mp3')),
    "watermelon": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'watermelon.mp3')),
    "orange": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'orange.mp3')),
    "pineapple": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'pineapple.mp3')),
    "cherries": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'cherries.mp3')),
    #"strawberry": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'strawberry.mp3')),
    "lemon": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'lemon.mp3')),
    "coconut": pygame.mixer.Sound(os.path.join(FRUIT_SOUNDS_FOLDER, 'coconut.mp3')),
}


# # Fruit processes
# FRUIT_PROCESSES = {
#     "🍎": {"color": (255, 0, 0), "name": "Total CPU Usage", "func": psutil.cpu_percent},
#     "🍌": {"color": (255, 255, 0), "name": "Virtual Memory Usage", "func": lambda: psutil.virtual_memory().percent},
#     "🍇": {"color": (128, 0, 128), "name": "Disk Usage", "func": lambda: psutil.disk_usage('/').percent},
#     "🍉": {"color": (255, 0, 255), "name": "Network Sent", "func": lambda: psutil.net_io_counters().bytes_sent},
#     "🍊": {"color": (255, 165, 0), "name": "Network Received", "func": lambda: psutil.net_io_counters().bytes_recv},
#     "🍍": {"color": (255, 255, 0), "name": "Swap Memory Usage", "func": lambda: psutil.swap_memory().percent},
#     "🍒": {"color": (255, 0, 0), "name": "CPU Load (1 min)", "func": lambda: psutil.getloadavg()[0]},
#     #"🍓": {"color": (255, 0, 0), "name": "CPU Frequency", "func": lambda: psutil.cpu_freq().current if psutil.cpu_freq() else "N/A"},
#     "🍋": {"color": (255, 255, 0), "name": "System Uptime", "func": lambda: int(time.time() - psutil.boot_time())},
#     "🥥": {"color": (128, 128, 128), "name": "Number of Processes", "func": lambda: len(psutil.pids())},
# }

# Fruit processes with sound file names
FRUIT_PROCESSES = {
    "🍎": {"color": (255, 0, 0), "name": "Total CPU Usage", "func": psutil.cpu_percent, "sound": "apple.mp3"},
    "🍌": {"color": (255, 255, 0), "name": "Virtual Memory Usage", "func": lambda: psutil.virtual_memory().percent, "sound": "banana.mp3"},
    "🍇": {"color": (128, 0, 128), "name": "Disk Usage", "func": lambda: psutil.disk_usage('/').percent, "sound": "grapes.mp3"},
    "🍉": {"color": (255, 0, 255), "name": "Network Sent", "func": lambda: psutil.net_io_counters().bytes_sent, "sound": "watermelon.mp3"},
    "🍊": {"color": (255, 165, 0), "name": "Network Received", "func": lambda: psutil.net_io_counters().bytes_recv, "sound": "orange.mp3"},
    "🍍": {"color": (255, 255, 0), "name": "Swap Memory Usage", "func": lambda: psutil.swap_memory().percent, "sound": "pineapple.mp3"},
    "🍒": {"color": (255, 0, 0), "name": "CPU Load (1 min)", "func": lambda: psutil.getloadavg()[0], "sound": "cherries.mp3"},
    # "🍓": {"color": (255, 0, 0), "name": "CPU Frequency", "func": lambda: psutil.cpu_freq().current if psutil.cpu_freq() else "N/A", "sound": "strawberry.mp3"},
    "🍋": {"color": (255, 255, 0), "name": "System Uptime", "func": lambda: int(time.time() - psutil.boot_time()), "sound": "lemon.mp3"},
    "🥥": {"color": (128, 128, 128), "name": "Number of Processes", "func": lambda: len(psutil.pids()), "sound": "coconut.mp3"},
}



class SnakeGame:
    def __init__(self):
        self.snake = [(0, 0)]
        self.direction = (1, 0)
        self.fruit = self._generate_fruit()
        self.game_over = False
        self.score = 0
        self.high_score = self.load_high_score()
        self.message = ""

    # def _generate_fruit(self):
    #     while True:
    #         fruit_position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
    #                           random.randint(0, (GAME_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
    #         fruit_emoji = random.choice(list(FRUIT_PROCESSES.keys()))
    #         if fruit_position not in self.snake:
    #             return fruit_position, fruit_emoji
    def _generate_fruit(self):
        while True:
            fruit_position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                              random.randint(0, (GAME_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
            fruit_emoji = random.choice(list(FRUIT_PROCESSES.keys()))
            if fruit_position not in self.snake:
                # Play the sound for the new fruit
                fruit_name = FRUIT_PROCESSES[fruit_emoji]['name'].split()[0].lower()
                if fruit_name in FRUIT_SOUNDS:
                    fruit_sound_channel.play(FRUIT_SOUNDS[fruit_name])
                return fruit_position, fruit_emoji


    def move_snake(self):
        if self.game_over:
            return

        new_head = ((self.snake[0][0] + self.direction[0] * GRID_SIZE) % WIDTH,
                    (self.snake[0][1] + self.direction[1] * GRID_SIZE) % GAME_HEIGHT)

        if new_head in self.snake:
            self.game_over = True
        else:
            self.snake = [new_head] + self.snake[:-1]

            if new_head == self.fruit[0]:
                self.snake.append(self.snake[-1])
                self._consume_fruit()
                self.fruit = self._generate_fruit()

    # def _consume_fruit(self):
    #     fruit_emoji = self.fruit[1]
    #     process = FRUIT_PROCESSES[fruit_emoji]
    #     stat = process['func']()
        
    #     # Update the message to include the emoji
    #     self.message = f"{fruit_emoji} {process['name']}: {stat}"

    #     self.score += 1  # Increase score

    #     # Update high score if necessary
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #         self.save_high_score(self.high_score)

    #     # Determine the fruit name from the emoji
    #     fruit_name = process['name'].split()[0].lower()

    #     # Play sound for the consumed fruit
    #      # Play sound for the consumed fruit
    #     if fruit_name in FRUIT_SOUNDS:
    #         fruit_sound_channel.play(FRUIT_SOUNDS[fruit_name])  # Play on the allocated channel


    #     # Extend the snake's length
    #     self.snake.append(self.snake[-1])

    #     # Generate a new fruit
    #     self.fruit = self._generate_fruit()

    def _consume_fruit(self):
        fruit_emoji = self.fruit[1]
        process = FRUIT_PROCESSES[fruit_emoji]
        stat = process['func']()
        
        # Update the message to include the emoji
        self.message = f"{fruit_emoji} {process['name']}: {stat}"

        self.score += 1  # Increase score

        # Update high score if necessary
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score(self.high_score)

        # Play sound for the consumed fruit
        fruit_sound_file = process.get("sound")
        if fruit_sound_file and os.path.exists(os.path.join(FRUIT_SOUNDS_FOLDER, fruit_sound_file)):
            pygame.mixer.music.stop()  # Stop any currently playing music
            pygame.mixer.music.load(os.path.join(FRUIT_SOUNDS_FOLDER, fruit_sound_file))
            pygame.mixer.music.play()

        # Extend the snake's length
        self.snake.append(self.snake[-1])

        # Generate a new fruit
        self.fruit = self._generate_fruit()


    def change_direction(self, new_direction):
        if not self.game_over and (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))

        fruit_position, fruit_emoji = self.fruit
        fruit_image = FRUIT_IMAGES[fruit_emoji]
        screen.blit(fruit_image, fruit_position)

        pygame.draw.rect(screen, (200, 200, 200), (0, GAME_HEIGHT, WIDTH, PANEL_HEIGHT))

        # Check if the last consumed fruit and its stat are available
        if hasattr(self, 'last_fruit_emoji') and hasattr(self, 'last_fruit_stat'):
            # Draw the last consumed fruit emoji
            last_fruit_image = FRUIT_IMAGES[self.last_fruit_emoji]
            screen.blit(last_fruit_image, (5, GAME_HEIGHT + 5))

            # Display the corresponding system statistic
            stat_text = f"{FRUIT_PROCESSES[self.last_fruit_emoji]['name']}: {self.last_fruit_stat}"
            stat_surface = FONT.render(stat_text, True, (0, 0, 0))
            screen.blit(stat_surface, (40, GAME_HEIGHT + 5))

        text_surface = FONT.render(self.message, True, (0, 0, 0))
        screen.blit(text_surface, (5, GAME_HEIGHT + 5))

        score_text = FONT.render(f"Score: {self.score}", True, (0, 0, 0))
        high_score_text = FONT.render(f"High Score: {self.high_score}", True, (0, 0, 0))
        screen.blit(score_text, (5, GAME_HEIGHT + 25))
        screen.blit(high_score_text, (WIDTH - 150, GAME_HEIGHT + 25))


    def load_high_score(self):
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        return 0

    def save_high_score(self, high_score):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(high_score))



def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('FruitPunch Games Presents: Snakes in the Operating System!!!')
    clock = pygame.time.Clock()
    game = SnakeGame()

    # Load title screen image
    title_screen = pygame.transform.scale(pygame.image.load("snake-game-image.png"), (WIDTH, HEIGHT))
    global game_state  # Access the global game_state variable

    start_font = pygame.font.Font(None, 72)  # Increase the font size to 36


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_state == MENU:
                    if event.key == pygame.K_s:  # Press 'S' to start the game
                        game_state = GAME
                        game = SnakeGame()  # Reset the game
                elif game_state == GAME:
                    if game.game_over:
                        if event.key == pygame.K_r:
                            game = SnakeGame()
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                    else:
                        if event.key == pygame.K_UP:
                            game.change_direction((0, -1))
                        elif event.key == pygame.K_DOWN:
                            game.change_direction((0, 1))
                        elif event.key == pygame.K_LEFT:
                            game.change_direction((-1, 0))
                        elif event.key == pygame.K_RIGHT:
                            game.change_direction((1, 0))

        screen.fill((0, 0, 0))

        if game_state == MENU:
            screen.blit(title_screen, (0, 0))  # Display the title screen
            start_text = FONT.render("Press 'S' to Start", True, (255, 255, 255))
            screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
        elif game_state == GAME:
            if not game.game_over:
                game.move_snake()
            game.draw(screen)
            if game.game_over:
                game_over_text = FONT.render("Game Over! Press 'R' to Restart or 'Q' to Quit", True, (255, 0, 0))
                screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()


