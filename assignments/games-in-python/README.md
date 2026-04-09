# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python, practicing string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game Structure

#### Description
Create the core structure for the Hangman game, including word selection and game state tracking.

#### Requirements
Completed program should:

- Define a list of words for the game to randomly select from
- Use `random.choice()` to pick a word at the start of each game
- Track which letters the player has guessed
- Track the number of incorrect guesses remaining (start with 6)

### 🛠️ Implement the Game Loop

#### Description
Write the main game loop that accepts player input, updates the game state, and displays progress each turn.

#### Requirements
Completed program should:

- Display the current word progress using `_` for unguessed letters (e.g., `_ _ a _ _`)
- Prompt the player to guess a letter each turn
- Update the display when a correct letter is guessed
- Decrease remaining attempts on an incorrect guess
- End the game when the word is fully guessed or attempts are exhausted
- Display a win or lose message at the end
