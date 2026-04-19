# Car Game

A small **Pygame** maze game: you drive a car through a factory layout loaded from a CSV map, with an optional text menu for instructions and file logging for the operator session.

Originally written as a coursework-style autonomous-vehicle exercise (2018).

## Prerequisites

- **Python 3** (3.8+ recommended)
- **[Pygame](https://www.pygame.org/)**

## Setup

Create a virtual environment (recommended), then install Pygame:

```bash
cd car-game
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pygame
```

## Run

From the project directory:

```bash
python Car_Game.py
```

The program asks for your name, then shows a **numbered menu** (basic / technical / expert / context help, start, or exit). Choose **5** to start the graphical run. The window shows the maze; movement uses the keyboard (see below). Closing the window ends the run.

## Controls (in-game)

| Keys | Action |
|------|--------|
| **W** / **↑** | Move up |
| **S** / **↓** | Move down |
| **A** / **←** | Move left |
| **D** / **→** | Move right |
| **I** | In-game help (as implemented in the game loop) |

## Data files

| File | Role |
|------|------|
| `Rafal_Factory.csv` | Factory / maze grid used as the map |
| `ZAC15107943.txt` | Append-only session log (created/updated when you run) |

## Project layout

| Path | Contents |
|------|----------|
| `Car_Game.py` | Entry point: menu, pygame loop, logging |
| `genMaze.py` | Maze loading, pygame window, rendering |
| `car.py` | Car / movement logic |
| `Library_File_1.py` | User input helpers and log file I/O |
| `Library_File_Help.py` | Printed help text for the menu |
| `Rafal_Factory.csv` | Map data |
| `ZAC15107943.txt` | Operator log output |

## Stack

- **Language:** Python 3  
- **Graphics / input:** [Pygame](https://www.pygame.org/)
