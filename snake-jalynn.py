import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FRUIT_PROCESSES = {
    "🍎": {"color": (255, 0, 0), "name": "Process A"},
    "🍌": {"color": (255, 255, 0), "name": "Process B"},
    "🍇": {"color": (128, 0, 128), "name": "Process C"},
    "🍉": {"color": (255, 0, 255), "name": "Process D"},
    "🍊": {"color": (255, 165, 0), "name": "Process E"},
}

# Initialize Pygame and set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

class SnakeGame:
    def __init__(self):
        self.snake = [(0, 0)]  # Initial position of the snake
        self.direction = (1, 0)  # Initial movement direction (right)
        self.fruit = self._generate_fruit()
        self.game_over = False

    def _generate_fruit(self):
        while True:
            fruit_position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                              random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
            fruit_emoji = random.choice(list(FRUIT_PROCESSES.keys()))
            if fruit_position not in self.snake:
                return fruit_position, fruit_emoji

    def move_snake(self):
        if self.game_over:
            return

        new_head = ((self.snake[0][0] + self.direction[0] * GRID_SIZE) % WIDTH,
                    (self.snake[0][1] + self.direction[1] * GRID_SIZE) % HEIGHT)

        if new_head in self.snake:
            self.game_over = True
        else:
            self.snake = [new_head] + self.snake[:-1]

            if new_head == self.fruit[0]:
                self.snake.append(self.snake[-1])
                self._consume_fruit()
                self.fruit = self._generate_fruit()

    def _consume_fruit(self):
        fruit_emoji = self.fruit[1]
        process = FRUIT_PROCESSES[fruit_emoji]
        print(f"The snake consumed resources from {process['name']} associated with {fruit_emoji}")

    def change_direction(self, new_direction):
        if not self.game_over:
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))

        fruit_position, fruit_emoji = self.fruit
        pygame.draw.rect(screen, FRUIT_PROCESSES[fruit_emoji]['color'], (*fruit_position, GRID_SIZE, GRID_SIZE))

def main():
    clock = pygame.time.Clock()
    game = SnakeGame()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    game.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    game.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    game.change_direction((1, 0))

        game.move_snake()

        screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.flip()

        clock.tick(10)

if __name__ == "__main__":
    main()
