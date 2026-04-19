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
python Car_Game.py
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
| `Rafal_Factory.csv` | Factory / maze map |
| `ZAC15107943.txt` | Session log (append) |

## Project structure

| Path | Role |
|------|------|
| `Car_Game.py` | Entry: menu, pygame loop, logging |
| `genMaze.py` | Maze load, window, rendering |
| `car.py` | Car movement |
| `Library_File_1.py` | Input helpers and log I/O |
| `Library_File_Help.py` | Printed help text |
| `Rafal_Factory.csv` | Map data |

## Stack

- **Language:** Python 3  
- **Graphics / input:** [Pygame](https://www.pygame.org/)
