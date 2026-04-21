# Car Game

## Description

A **Pygame** maze game: drive a car through a factory layout defined by a CSV map, with a text menu for help and file logging for the operator session. Coursework-style autonomous-vehicle exercise (2018).

## Prerequisites

- **Python 3** (3.8+ recommended)
- **[Pygame](https://www.pygame.org/)**

## Installation

```bash
cd car-game
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pygame
```

## Usage

```bash
python car_game.py
```

The program asks for your name, then shows a **numbered menu** (help levels, start, exit). Choose **5** to start the graphical run. Close the window to stop.

### Controls (in-game)

| Keys | Action |
|------|--------|
| **W** / **↑** | Move up |
| **S** / **↓** | Move down |
| **A** / **←** | Move left |
| **D** / **→** | Move right |
| **I** | In-game help |

### Data files

| File | Role |
|------|------|
| `factory_map.csv` | Factory / maze map |
| `session_log.txt` | Session log (append) |

## Project structure

| Path | Role |
|------|------|
| `car_game.py` | Entry: menu, pygame loop, logging |
| `gen_maze.py` | Maze load, window, rendering |
| `car.py` | Car movement |
| `session_io.py` | Input prompts and append-only session log |
| `help_text.py` | Printed help text for the menu |
| `factory_map.csv` | Map data |

All Python modules use **snake_case** file names (PEP 8).

## Stack

- **Language:** Python 3  
- **Graphics / input:** [Pygame](https://www.pygame.org/)
