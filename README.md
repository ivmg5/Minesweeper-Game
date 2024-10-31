# **Minesweeper**
> *An interactive command-line implementation of Minesweeper, designed to engage cognitive skills and provide challenging gameplay.*

## **Introduction**
This project is a Python-based implementation of the classic Minesweeper game, designed to run in the command-line interface. It allows users to interactively play the game by revealing cells and trying to avoid mines, providing feedback on cell contents (numbers, empty cells, or mines) as they play.

## **Project Description**
- **Main functionality:** Minesweeper game with interactive cell selection, bomb detection, and win/lose conditions.
- **Justification of cognitive skills:** 
  - **Memory:** Players need to remember suspicious mine locations.
  - **Pattern recognition:** Analyzing cell numbers to infer mine positions.
  - **Brain stimulation:** Solving the game requires significant mental effort.
  - **Stress management:** The risk of uncovering a mine can create stress, requiring players to manage it for successful gameplay.
- **Background:** Research in an elderly care facility showed that playing games like Minesweeper enhanced cognitive abilities and overall well-being. Daniel Goleman’s book *Focus* documents a similar case where consistent gameplay led to impressive performance gains.
- **Challenges faced:** The primary design challenge involved implementing the logic to reveal multiple cells when an empty cell (one without nearby mines) is uncovered. This solution required layered conditional logic and a predetermined board design.
- **Technologies used:** Python, standard libraries (`os`).
- **Future improvements:** Potential upgrades could include additional difficulty levels, user-defined board sizes, and enhanced recursive cell reveal logic.

## **Table of Contents**
1. [Introduction](#introduction)
2. [Project Description](#project-description)
3. [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)

## **Installation**
1. **Prerequisites**:
   - **Python 3.x** - [Download Python](https://www.python.org/downloads/)

2. **Clone the repository:**
   ```bash
   git clone https://github.com/ivmg5/Minesweeper-Game.git
   cd Minesweeper-Game
   ```

3. **Run the project:**
   ```bash
   python main.py
   ```

### **Configuration Options**
- This project does not require additional configurations. However, make sure your terminal is large enough to display the full board.

## **Usage**
### How to Play:
1. Start the game by running the script with Python.
2. Enter the row and column numbers of the cell you wish to reveal.
3. Continue revealing cells while avoiding bombs. The game ends when all non-bomb cells are revealed (win) or a bomb is uncovered (lose).

### Example usage:
```bash
python main.py
# Prompts will ask for row and column input
```

## **License**
This project is licensed under the MIT License.

[![Build Status](https://img.shields.io/badge/status-active-brightgreen)](#)
[![Code Coverage](https://img.shields.io/badge/coverage-80%25-yellowgreen)](#)
