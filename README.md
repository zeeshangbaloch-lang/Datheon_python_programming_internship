# Datheon Python Internship

This repository contains my completed tasks for the Datheon Python Internship.

**Author:** Muhammad Zeeshan

## Completed Tasks

| Task | Project | Folder | Status |
|------|---------|--------|--------|
| 1 | Hangman Word Guessing Game (Console) | `Task1_Hangman/` | Done |
| 2 | Stock Portfolio Performance Tracker | `Task2_Stock_Portfolio_Tracker/` | Done |

---

## Task 1: Hangman Word Guessing Game (Console)

A terminal-based Hangman game written in Python 3. The player guesses a hidden word one letter at a time and loses after 6 wrong guesses.

### Features

* Random secret word chosen with `random.choice()`
* ASCII gallows art that updates after every wrong guess
* Word shown as blanks that fill in as you guess (e.g. `p _ _ h o _`)
* Shows all wrong letters guessed so far
* Repeated letters are ignored with a message, with **no penalty**
* Input validation (only a single letter a-z is accepted)
* Clear victory and game-over screens that reveal the word

### Requirements

* Python 3.8 or newer
* No extra libraries needed (uses only the standard library: `random`)

### Installation

1. Clone this repository:

   ```
   git clone https://github.com/zeeshangbaloch-lang/Datheon_Python_Programming_Internship.git
   ```

2. Go into the project folder:

   ```
   cd Datheon_Python_Programming_Internship/Task1_Hangman
   ```

### How to Run

```
python hangman_improved.py
```

On some systems use `python3 hangman_improved.py` instead.

### How to Play

1. The game shows the gallows and a row of blanks, one for each letter.
2. Type one letter and press Enter.
3. A correct letter is revealed in every place it appears.
4. A wrong letter adds a part to the hangman. You can make 6 wrong guesses.
5. Guess the whole word before the drawing is complete to win.

### Code Overview

| Part | What it does |
|------|--------------|
| `secret` | List of possible secret words |
| `STAGES` | List of 7 ASCII drawings (0 to 6 mistakes) |
| `show_game()` | Prints the gallows, the masked word, wrong letters and tries left |
| `play()` | Runs one full game: input, validation, win/lose checks |

Key design choices:

* A `set` called `guessed` stores every letter tried, so a repeated letter is detected before any penalty is applied.
* The mistake count is used as the index into `STAGES`, so the correct picture is shown without long `if/else` chains.

### Example Output

```
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========

Word: _ a _ _ _ _
Wrong letters: x z
Tries left: 4
```

---

## Task 2: Stock Portfolio Performance Tracker

A console program that tracks a stock portfolio. The user enters ticker symbols, buy prices, number of shares and current prices. The program calculates the gain or loss for every holding, shows the total portfolio value, and saves the results to a CSV file.

### Features

* Add as many stocks as you like (type `done` to finish)
* Holdings stored in a dictionary, with the ticker symbol as the key
* Calculates amount invested, current value and percentage gain/loss per stock
* Shows total invested, total portfolio value and overall percentage result
* Formatted table printed in the console
* Results saved automatically to `portfolio_summary.csv` using Python's `csv` module
* Input validation (numbers only, and buy price and shares must be above 0)

### Requirements

* Python 3.8 or newer
* No extra libraries needed (uses only the standard library: `csv`)

### How to Run

```
cd Datheon_Python_Programming_Internship/Task2_Stock_Portfolio_Tracker
python portfolio.py
```

On some systems use `python3 portfolio.py` instead.

### How to Use

1. Type a ticker symbol, for example `AAPL`.
2. Enter the buy price, the number of shares and the current price.
3. Repeat for more stocks, or type `done` to finish.
4. The summary table is printed and saved to `portfolio_summary.csv`.

### Formulas Used

| Value | Formula |
|-------|---------|
| Amount invested | buy price x shares |
| Current value | current price x shares |
| Gain/Loss % | (current value - amount invested) / amount invested x 100 |

### Example Output

```
Ticker    Shares       Buy       Now    Invested       Value   Gain/Loss
------------------------------------------------------------------------------
AAPL       10.00    150.00    180.00     1500.00     1800.00     +20.00%
TSLA        5.00    200.00    170.00     1000.00      850.00     -15.00%
------------------------------------------------------------------------------
Total invested : 2500.00
Total value    : 2650.00
Overall result : +6.00%
```

---

## Project Structure

```
Datheon_Python_Programming_Internship/
├── README.md
├── Task1_Hangman/
│   └── hangman_improved.py
└── Task2_Stock_Portfolio_Tracker/
    ├── portfolio.py
    └── portfolio_summary.csv
```

## Author

Muhammad Zeeshan
