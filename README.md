# Lighthouse Space Invaders

A Python-based Space Invaders game developed as part of **Project Lighthouse at Kiel University (Christian-Albrechts-Universität zu Kiel)**. The game was designed to run on the university's Lighthouse installation, which uses the windows of the university high-rise building as a large-scale LED display.

## About the Project

The game was developed collaboratively during a two-week university programming project in a team of two.

The objective was to create an interactive arcade game for the Lighthouse display. Inspired by Space Invaders, the game includes player movement, shooting mechanics, different enemy types, collision detection, scoring, increasing difficulty, and multiple game states.

## Features

- Player-controlled cannon with horizontal movement
- Projectile and shooting mechanics
- Multiple enemy types with randomized spawning
- Collision detection between projectiles and enemies
- Score tracking and increasing difficulty
- Start, game-over, and score screens
- Output to the Lighthouse LED installation

## Controls

- **Left Arrow:** Move left
- **Right Arrow:** Move right
- **Space:** Start the game / shoot / continue between game states

## Technologies

- Python
- Pygame Zero
- pygame
- pyghthouse

## Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Lighthouse authentication credentials are not included in this repository. Valid credentials are required to connect to the Lighthouse installation.

Run the game from the project directory:

```bash
python3 shootingstar.py
```

## Project Lighthouse & pyghthouse

The connection to the Lighthouse installation is implemented using the `pyghthouse` Python package.

The initial Lighthouse connection setup is based on the publicly available examples provided by `pyghthouse`.

- [pyghthouse on GitHub](https://github.com/ProjectLighthouseCAU/pyghthouse)
- [pyghthouse on PyPI](https://pypi.org/project/pyghthouse/)

## University Context

This project was developed as part of **Project Lighthouse at Kiel University (CAU)**.

Authentication credentials, API tokens, and registration keys are intentionally not included in this repository.