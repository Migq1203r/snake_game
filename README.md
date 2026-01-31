# Snake Game 🐍

A classic Snake Game implemented in Python using the built-in `turtle` graphics library.

The player controls a snake that grows in length every time it eats food. The game ends if the snake collides with the wall or with itself.

## Features

- Classic snake movement using keyboard controls
- Random food generation
- Score tracking
- Collision detection (walls and self)
- Simple and clean game loop

## Requirements

- Python 3.8+
- No external libraries required (uses Python standard library)

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/snake-game.git
cd snake-game
````

## Usage

Run the main game file:

```bash
python snake_game.py
```

## Controls

* **Up Arrow** – Move up
* **Down Arrow** – Move down
* **Left Arrow** – Move left
* **Right Arrow** – Move right

## Project Structure

```text
.
├── snake_game.py
├── snake.py
├── food.py
├── scoreboard.py
├── collision.py
└── README.md
```

### File Overview

* `snake_game.py` – Game loop and screen setup
* `snake.py` – Snake movement and growth logic
* `food.py` – Food creation and repositioning
* `scoreboard.py` – Score display and updates
* `collision.py` – Game over handling

## How It Works

* The game runs in a loop with screen updates every 0.1 seconds
* The snake grows when it eats food
* The game ends if the snake:

  * Hits the wall
  * Collides with its own body

## License

This project is licensed under the GNU GPL V3
