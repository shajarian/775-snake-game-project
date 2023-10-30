# 775-snake-game-project

```
Project Title: Integrating Snake Video Game into an Operating System
Group Member: Qinali Ma, Shaghayegh Shajarian, Ja’Lynn Joyce
Objective: Enhance the user experience of the operating system by integrating a gaming feature that most
are familiar with. The Snake video game aims to entertain and pay homage to the classic Snake game
while adapting it to modern technology. By integrating the game within the operating system, we aim to
improve user engagement and interaction while serving as a showcase of technical skills through the
game’s performance, efficiency, and compatibility.
Scope: The scope of this project is to integrate the class Snake video game into the operating system,
making it a built-in application. This will involve developing a user-friendly interface, gameplay features,
collision detection, scoring mechanisms, and more. Integration testing will be conducted to ensure the
game’s stability and compatibility with the operating system. Considering the OS metaphor:
Description: Use the Snake game as a metaphor for OS resource management. The snake represents
processes, and the fruits represent system resources (CPU, RAM, Disk, Network). As the snake consumes
resources, it grows. Hence, the player's goal is to manage the snake's growth without overloading the
system.
● The snake represents a process that requires resources (fruits).
● Consuming resources makes the process (snake) grow, symbolizing how processes use more
system resources over time.
● Hitting the boundary or colliding with itself is akin to a system crash or process failure, resulting
in a game-over.
Potential Data Setups:
1. Snake Game with Pygame
2. Snake Game Using Turtle in Python
3. Snake Game in Python
Ja’Lynn Joyce: Game Logic & Mechanics
Task: To develop the basic rules and gameplay mechanics.
Choose the Game:
● Define the initial position and length of the snake
○ The initial position represents the state of a process when it starts running in the system
or the initial resource consumption by the process.
● Movement mechanism: When an arrow key is pressed, move the snake in that direction.
○ Arrow keys represent user interactions or decisions that affect how a process utilizes
resources.
■ For example, moving the snake in a specific direction corresponds to making
resource allocation decisions for a process.
● Growing mechanism: When the snake eats a fruit, it gets longer.
○ This represents a process of acquiring additional resources during its execution.
■ The process's resource consumption increases as the snake grows longer.
■ This simulates dynamic resource allocation during a process's lifetime.
● End mechanism: If the snake hits itself or the screen border, the game ends.
○ This game-ending condition is a process failure due to resource contention or resource
overutilization
■ It mirrors how a process might terminate if it encounters resource conflicts or
exceeds resource limits
● Test Mechanisms Without Graphics: Just print out the results in text format, e.g., snake
coordinates, length, game over message.
○ The printed results can be seen as a representation of resource utilization and
management
■ The snake's coordinates and length can be interpreted as the state of a process in
terms of resource allocation and consumption
Qianli Ma: Graphics & User Interface
Task: To visually represent the game.
● Game Window: Create a simple window to display the game.
○ Visualize it as an OS environment where resource allocation and management take place
● Drawing the Snake: Represent the snake as a sequence of squares.
○ Represent the snake as a sequence of squares within the game window. These squares
symbolize a running process within the OS environment
■ The length and appearance of the snake can be indicative of a process's resource
consumption and growth
● Drawing the Fruit: Represent the fruit as a smaller square (or circle).
○ This smaller square or circle represents available system resources that a process can
consume.
○ The fruit's appearance may change to reflect the type of resource (e.g., CPU, RAM, Disk,
Network).
● User Input: Handle arrow key presses to control the direction of the snake.
○ These arrow key presses correspond to user-initiated resource allocation decisions.
■ The direction of the snake can be interpreted as the chosen path or resource
allocation strategy for the running process
Shaghayegh Shajarian: OS Interaction
Task: Make the game interact with the operating system.
● User Input: How key presses are captured from the operating system: 2 weeks
(This includes researching, implementing, and testing the mechanism to capture key presses,
which are basic arrow keys from the operating system.)
● Game Loop: Checks for user input, updates game state, and redraws the screen: 1.5 weeks
(Develop the basic game loop structure, integrate it with the user input, and ensure it can update
the game state and redraw the screen.)
● Delay/Sleep: Use time.sleep function to control the speed of the game loop and maintain a steady
pace for the game loop. This sets a consistent "CPU cycle" for the game's metaphorical OS.
(simulates task scheduling): 1.5 weeks
(Implement the time.sleep function to control the game speed, integrate it with the game loop, and
test different speeds for optimal gameplay.)





```
